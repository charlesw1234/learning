#include <stdint.h>
#include <stdlib.h>
#include "memcreate.h"

static void
showbin(void *buf, size_t szbuf)
{
    size_t cur, cur0;
    uint8_t *u8buf = (uint8_t *)buf;
    for (cur = 0; cur < szbuf; cur += 16) {
        printf("%04u: ", (unsigned)cur);
        for (cur0 = 0; cur0 < 16; ++cur0)
            if (cur + cur0 < szbuf) printf("%02X, ", u8buf[cur + cur0]);
        printf("\n");
    }
}

int
main(void)
{
    void *buf = NULL;
    size_t szbuf = 0;
    FILE *wfp = fopen_memcreate(&buf, &szbuf);
    fseek(wfp, 64, SEEK_SET);
    printf("wfp = %p\n", wfp);
    fwrite(&wfp, 1, sizeof(wfp), wfp);
    printf("%u: %u\n", __LINE__, (unsigned)ftell(wfp));
    fseek(wfp, 0, SEEK_SET);
    fclose(wfp);
    printf("buf = %p, szbuf = %u\n", buf, (unsigned)szbuf);
    showbin(buf, szbuf);
    free(buf);
    return 0;
}
