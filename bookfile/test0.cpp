#include <stdlib.h>
#include "bookfile.hpp"

const unsigned num_chapters = 256;
const unsigned max_blocks = 256;
int
main(void)
{
    bool succ;
    unsigned idx, idx0;
    bookfile::bookfile_t bfobj("test.book", 4);
    uint64_t chapterid_list[num_chapters];
    uint32_t blocks_list[num_chapters], blocks;
    uint8_t data[bookfile::size_block * max_blocks];

    for (idx = 0; idx < num_chapters; ++idx) {
        do {
            chapterid_list[idx] = (uint64_t)random();
            for (idx0 = 0; idx0 < idx; ++idx0)
                if (chapterid_list[idx0] == chapterid_list[idx]) break;
        } while (idx0 < idx);
        blocks_list[idx] = (uint32_t)(random() % (max_blocks - 1) + 1);
        printf("%u: %s, %lu, %u\n", idx,
               bfobj.insert(chapterid_list[idx], blocks_list[idx]) ? "true": "false",
               (unsigned long)chapterid_list[idx], (unsigned)blocks_list[idx]);
    }
    for (idx = 0; idx < num_chapters; ++idx) {
        succ = bfobj.seek(chapterid_list[idx], &blocks);
        if (!succ || blocks != blocks_list[idx])
            printf("%u: %s, %u, %u\n", idx, succ ? "true": "false",
                   (unsigned)blocks, (unsigned)(blocks_list[idx]));
        for (unsigned idx0 = 0; idx0 < bookfile::size_block * blocks; ++idx0) data[idx0] = idx;
        bfobj.write(data, blocks);
    }
    return 0;
}
