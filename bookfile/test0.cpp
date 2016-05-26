#include <stdlib.h>
#include "bookfile.hpp"

const unsigned num_chapters = 256;
const unsigned max_blocks = 256;
int
main(void)
{
    bookfile::bookfile_t bfobj("test0.book", 4);
    uint64_t chapterid_list[num_chapters];
    uint32_t blocks_list[num_chapters], blocks;
    uint8_t data[bookfile::size_block * max_blocks];

    for (unsigned idx = 0; idx < num_chapters; ++idx) {
        chapterid_list[idx] = (uint64_t)random();
        blocks_list[idx] = (uint32_t)(random() % max_blocks);
        printf("%u: %s\n", idx,
               bfobj.insert(chapterid_list[idx], blocks_list[idx]) ? "true": "false");
    }
    for (unsigned idx = 0; idx < num_chapters; ++idx) {
        printf("%u: %s, %u, %u\n", idx,
               bfobj.seek(chapterid_list[idx], &blocks) ? "true": "false",
               (unsigned)blocks, (unsigned)(blocks_list[idx]));
        for (unsigned idx0 = 0; idx0 < bookfile::size_block * blocks; ++idx0) data[idx0] = idx;
        bfobj.write(data, blocks);
    }
    return 0;
}
