#include <stdlib.h>
#include "bookfile.hpp"

const unsigned num_chapters = 256;
const unsigned max_blocks = 256;
int
main(void)
{
    unsigned idx, idx0;
    bookfile::bookfile_t bfobj("test.book", num_chapters);
    bookfile::chapter_t chapters[num_chapters];
    const bookfile::chapter_t *seekout;
    uint8_t data[bookfile::size_block * max_blocks];

    for (idx = 0; idx < num_chapters; ++idx) {
        do {
            chapters[idx].chapterid = (uint64_t)random();
            for (idx0 = 0; idx0 < idx; ++idx0)
                if (chapters[idx0].chapterid == chapters[idx].chapterid) break;
        } while (idx0 < idx);
        chapters[idx].blocks = (uint32_t)(random() % (max_blocks - 1) + 1);
        chapters[idx].md5part0 = chapters[idx].md5part1 = 0xA0A1A2A3A4A5A6A7UL;
        printf("%u: %s, %lu, %u\n", idx, bfobj.insert(chapters + idx) ? "true": "false",
               (unsigned long)chapters[idx].chapterid, (unsigned)chapters[idx].blocks);
    }
    printf("sanity: %s\n", bfobj.sanity() ? "true": "false");
    for (idx = 0; idx < num_chapters; ++idx) {
        seekout = bfobj.seek(chapters[idx].chapterid);
        if (seekout == NULL) {
            printf("%u: false, %u\n", idx, (unsigned)chapters[idx].blocks);
        } else if (seekout->blocks != chapters[idx].blocks) {
            printf("%u: true, %u, %u\n", idx,
                   (unsigned)seekout->blocks, (unsigned)chapters[idx].blocks);
        } else {
            for (unsigned idx0 = 0; idx0 < bookfile::size_block * seekout->blocks; ++idx0)
                data[idx0] = idx;
            bfobj.write(data, seekout->blocks);
        }
    }
    printf("sanity: %s\n", bfobj.sanity() ? "true": "false");
    return 0;
}
