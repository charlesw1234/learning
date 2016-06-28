#include "beecrypt/sha384.h"

static const char *hex = "0123456789abcdef";
static void
hexprint(byte value)
{
    printf("%c%c", hex[value >> 4], hex[value & 0xF]);
}
int
main(int argc, char *argv[])
{
    int idx;
    sha384Param param;
    byte digest[48], *cur;
    for (idx = 1; idx < argc; ++idx) {
        sha384Reset(&param);
        sha384Update(&param, (const byte *)argv[idx], strlen(argv[idx]));
        sha384Digest(&param, digest);
        for (cur = digest; cur < digest + sizeof(digest); ++cur)
            hexprint(*cur);
        printf("\n");
    }
    return 0;
}
