#include "zlib.h"

int
main(void)
{
    gzFile wfp = gzopen("xxx.gz", "wb9");
    gzclose(wfp);
    return 0;
}
