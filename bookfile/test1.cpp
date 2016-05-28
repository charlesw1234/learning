#include <stdlib.h>
#include "bookfile.hpp"

const unsigned max_blocks = 256;
int
main(void)
{
    bookfile::chapter_t *cur0;
    bookfile::chapter_hash_t *cur;
    const bookfile::chapter_t *seekout;
    bookfile::bookfile_t bfobj("test.book");
    uint8_t data[bookfile::size_block * max_blocks];

    printf("sanity: %s\n", bfobj.sanity() ? "true": "false");
    for (unsigned idx = 0; idx < bfobj.size(); ++idx) {
        cur = &bfobj[idx];
        for (unsigned idx0 = 0; idx0 < bookfile::num_chapter_hash; ++idx0) {
            cur0 = cur->chapters + idx0;
            if (cur0->blank()) continue;
            else if (cur0->removed()) continue;
            printf("chapter: %lu, %u blocks at %u\n", (unsigned long)cur0->chapterid,
                   (unsigned)cur0->blocks, (unsigned)cur0->position);
            seekout = bfobj.seek(cur0->chapterid);
            if (seekout && seekout->blocks == cur0->blocks) {
                if (bfobj.read(data, seekout->blocks) == seekout->blocks &&
                    !memcmp(data, data + 1, bookfile::size_block * seekout->blocks - 1))
                    continue;
            }
            printf("data check failed\n");
        }
    }
    return 0;
}
