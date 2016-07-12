#include <stdio.h>

int
main(void)
{
    char *buf;
    size_t szbuf;
    FILE *wfp = open_memstream(&buf, &szbuf);
    fseek(wfp, 1024, SEEK_SET);
    fwrite(&szbuf, 1, sizeof(szbuf), wfp);
    printf("%u: %u\n", __LINE__, (unsigned)ftell(wfp));
    fclose(wfp);
    printf("buf = %p, szbuf = %u\n", buf, (unsigned)szbuf);
    return 0;
}
