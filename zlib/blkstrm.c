#include <sys/time.h>
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <zlib.h>

#define BUFSZ 2048
static const unsigned long prompt_step = 16 * 1024 * 1024;

typedef struct {
    const char *fname;
    size_t size;
}  info_t;
static const info_t infos[] = {
    { "ssel2_quotation", 1232 },
    { "ssel2_index", 112 },
    { "ssel2_transactino", 96 },
    { "szsel2_quotation", 1080 },
    { "szsel2_index", 112 },
    { "szsel2_order", 64 },
    { "szsel2_transaction", 72 }
};
static const unsigned ninfos = sizeof(infos) / sizeof(infos[0]);

static void
process(const char *fname, size_t recsz)
{
    int rc;
    z_stream strm0, strm1;
    struct timeval tv0, tv1, tv2;
    unsigned long prompt = prompt_step;
    uint8_t buf0[BUFSZ], buf1[BUFSZ], buf2[BUFSZ];
    // setup.
    FILE *rfp = fopen(fname, "rb");
    if (rfp == NULL) return;
    memset(&strm0, 0, sizeof(strm0));
    memset(&strm1, 0, sizeof(strm1));
    assert(recsz < BUFSZ);
    rc = deflateInit(&strm0, 9);
    assert(rc == Z_OK);
    rc = inflateInit(&strm1);
    assert(rc == Z_OK);
    // one loop for a record.
    gettimeofday(&tv0, NULL); tv1 = tv0;
    while ((rc = fread(buf0, 1, recsz, rfp)) > 0) {
        // compress a record.
        assert(rc == recsz);
        strm0.next_in = buf0;
        strm0.avail_in = recsz;
        strm0.next_out = buf1;
        strm0.avail_out = sizeof(buf1);
        rc = deflate(&strm0, Z_SYNC_FLUSH);
        assert(rc == Z_OK);
        // decompress a record.
        strm1.next_in = buf1;
        strm1.avail_in = strm0.next_out - buf1;
        strm1.next_out = buf2;
        strm1.avail_out = sizeof(buf2);
        rc = inflate(&strm1, Z_SYNC_FLUSH);
        assert(rc == Z_OK);
        assert(strm1.next_out - buf2 == recsz);
        assert(memcmp(buf0, buf2, recsz) == 0);
        // report for each prompt step.
        if (strm0.total_in >= prompt) {
            gettimeofday(&tv2, NULL);
            printf("%lu bytes processed: %lu.\n", (unsigned long)strm0.total_in,
                   (tv2.tv_sec - tv1.tv_sec) * 1000 * 1000 +
                   (tv2.tv_usec - tv1.tv_usec));
            tv1 = tv2;
            prompt += prompt_step;
        }
    }
    gettimeofday(&tv2, NULL);
    printf("%lu bytes processed: %lu.\n", (unsigned long)strm0.total_in,
           (tv2.tv_sec - tv1.tv_sec) * 1000 * 1000 +
           (tv2.tv_usec - tv1.tv_usec));
    // terminate the input.
    strm0.next_in = buf0;
    strm0.avail_in = 0;
    strm0.next_out = buf1;
    strm0.avail_out = sizeof(buf1);
    rc = deflate(&strm0, Z_FINISH);
    assert(rc == Z_STREAM_END);
    rc = deflateEnd(&strm0);
    // terminate the output.
    strm1.next_in = buf1;
    strm1.avail_in = strm0.next_in - buf1;
    strm1.next_out = buf2;
    strm1.avail_out = sizeof(buf2);
    rc = inflate(&strm1, Z_FINISH);
    assert(rc == Z_STREAM_END);
    assert(strm1.next_out == buf2);
    fclose(rfp);
    // dump informations.
    gettimeofday(&tv2, NULL);
    printf("[%s/%u]: %lu / %lu = %f%% in %lu\n", fname, (unsigned)recsz,
           (unsigned long)strm0.total_out,
           (unsigned long)strm0.total_in,
           100 * (double)strm0.total_out / (double)strm0.total_in,
           (tv2.tv_sec - tv0.tv_sec) * 1000 * 1000 +
           (tv2.tv_usec - tv0.tv_usec));
}

int
main(int argc, char *argv[])
{
    int argidx;
    unsigned infoidx;
    for (argidx = 1; argidx < argc; ++argidx) {
        for (infoidx = 0; infoidx < ninfos; ++infoidx)
            if (!strcmp(infos[infoidx].fname, argv[argidx]))
                process(infos[infoidx].fname, infos[infoidx].size);
    }
    return 0;
}
