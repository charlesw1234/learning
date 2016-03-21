#include <stdio.h>
#include "scanner.hpp"

#if 0
static void
show(nametree::unichar_t *buf, size_t nchars)
{
    uint8_t utf8str[1024];
    // convert utf16 to utf8 chars.
    UTF16ToUTF8(buf, buf + nchars + 1, utf8str, utf8str + sizeof(utf8str));
    printf("(%3u): [%s]\n", (unsigned)nchars, utf8str);
}
#endif

int
main(int argc, char *argv[])
{
    const char *title;
    scanner::Scanner_t *sobj;
    for (int argidx = 1; argidx < argc; ++argidx) {
        sobj = new scanner::Scanner_t("bookinfo.txt.gz");
        while ((title = sobj->scan(argv[argidx])) != NULL)
            printf("[%s]\n", title);
        delete sobj;
    }
    return 0;
}
