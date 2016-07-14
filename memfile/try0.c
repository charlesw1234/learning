#include <stdint.h>
#include <stdlib.h>
#include "memcreate.h"

static void
showbin(memcreate_t *self)
{
    size_t cur, cur0;
    for (cur = 0; cur < self->size; cur += 16) {
        printf("%04u: ", (unsigned)cur);
        for (cur0 = 0; cur0 < 16; ++cur0)
            if (cur + cur0 < self->size) printf("%02X, ", self->body[cur + cur0]);
        printf("\n");
    }
}

int
main(void)
{
    memcreate_t mcobj;
    init_memcreate(&mcobj);
    FILE *wfp = fopen_memcreate(&mcobj);
    fseek(wfp, 64, SEEK_SET);
    printf("wfp = %p\n", wfp);
    fwrite(&wfp, 1, sizeof(wfp), wfp);
    printf("%u: %u\n", __LINE__, (unsigned)ftell(wfp));
    fseek(wfp, 0, SEEK_SET);
    fclose(wfp);
    printf("buf = %p, szbuf = %u\n", mcobj.body, (unsigned)mcobj.size);
    showbin(&mcobj);
    free_memcreate(&mcobj);
    return 0;
}
