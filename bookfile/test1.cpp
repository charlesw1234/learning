#include <stdlib.h>
#include "bookfile.hpp"

const unsigned max_blocks = 256;
int
main(void)
{
    bool succ;
    uint32_t blocks;
    bookfile::chapter_t *cur0;
    bookfile::chapter_hash_t *cur;
    bookfile::bookfile_t bfobj("test.book");
    uint8_t data[bookfile::size_block * max_blocks];

    for (unsigned idx = 0; idx < bfobj.size(); ++idx) {
        cur = &bfobj[idx];
        for (unsigned idx0 = 0; idx0 < bookfile::num_chapter_hash; ++idx0) {
            cur0 = cur->chapters + idx0;
            if (cur0->blank()) continue;
            else if (cur0->removed()) continue;
            printf("chapter: %lu, %u blocks at %u\n", (unsigned long)cur0->chapterid,
                   (unsigned)cur0->blocks, (unsigned)cur0->position);
            succ = bfobj.seek(cur0->chapterid, &blocks);
            if (succ && blocks == cur0->blocks) {
                if (bfobj.read(data, blocks) == blocks &&
                    !memcmp(data, data + 1, bookfile::size_block * blocks - 1)) continue;
            }
            printf("data check failed\n");
        }
    }
    return 0;
}
