#include <stdlib.h>
#include "bookfile.hpp"

int
main(void)
{
    bookfile::chapter_t *cur0;
    bookfile::chapter_hash_t *cur;
    bookfile::bookfile_t bfobj("test.book");
    for (unsigned idx = 0; idx < bfobj.size(); ++idx) {
        cur = &bfobj[idx];
        for (unsigned idx0 = 0; idx0 < bookfile::num_chapter_hash; ++idx0) {
            cur0 = cur->chapters + idx0;
            if (cur0->blank()) continue;
            else if (cur0->removed()) continue;
            printf("chapter: %lu, %u blocks at %u\n", (unsigned long)cur0->chapterid,
                   (unsigned)cur0->blocks, (unsigned)cur0->position);
        }
    }
    return 0;
}
