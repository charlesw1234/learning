#include <stdio.h>
#include <stdlib.h>
#include "utf.h"
#include "nametree.hpp"

static void
show(nametree::unichar_t *buf, size_t nchars)
{
    uint8_t utf8str[1024];
    // convert utf16 to utf8 chars.
    UTF16ToUTF8(buf, buf + nchars + 1, utf8str, utf8str + sizeof(utf8str));
    printf("(%3u): [%s]\n", (unsigned)nchars, utf8str);
}

int
main(void)
{
    size_t realsz, maxsz = 2 * 1024 * 1024;
    FILE *rfp = fopen("bookinfo.bin", "rb");
    uint8_t *body = (uint8_t *)malloc(maxsz);
    realsz = fread(body, 1, maxsz, rfp);
    printf("%u bytes read.\n", (unsigned)realsz);
    fclose(rfp);
    nametree::Tree_t treeobj(body);
    nametree::Iterator_t iterator(&treeobj);
    nametree::unichar_t buf[nametree::Iterator_t::MAXCHARS + 1];
    show(buf, iterator.get(buf));
    while (iterator.next())
        show(buf, iterator.get(buf));
    free(body);
    return 0;
}
