#ifdef _WIN32
#include <Time.h>
#include <Windows.h>
#else
#include <sys/time.h>
#endif
#include <stdio.h>
#include <vector>

#ifdef _WIN32
static const unsigned __int64 epoch = ((unsigned __int64) 116444736000000000ULL);
int
gettimeofday(struct timeval * tp, struct timezone * tzp)
{
    FILETIME    file_time;
    SYSTEMTIME  system_time;
    ULARGE_INTEGER ularge;

    GetSystemTime(&system_time);
    SystemTimeToFileTime(&system_time, &file_time);
    ularge.LowPart = file_time.dwLowDateTime;
    ularge.HighPart = file_time.dwHighDateTime;

    tp->tv_sec = (long) ((ularge.QuadPart - epoch) / 10000000L);
    tp->tv_usec = (long) (system_time.wMilliseconds * 1000);

    return 0;
}
#endif

unsigned
tvdiff(const struct timeval &tv0, const struct timeval &tv1)
{ return (1000 * 1000 *(tv0.tv_sec - tv1.tv_sec) + tv0.tv_usec) - tv1.tv_usec; }

typedef struct {
    long tv_sec;
    long tv_usec;
} Cell_t;

int
main(void)
{
    unsigned idx, diff0, diff1;
    unsigned sum0, sum1;
    struct timeval tv0, tv1, tv2;
    struct timeval tv00;
    std::vector<Cell_t> cellvector;
    std::vector<Cell_t>::const_iterator iter;

    for (idx = 0; idx < 10000000; ++idx) {
        gettimeofday(&tv00, NULL);
        Cell_t tmcell;
        tmcell.tv_sec = tv00.tv_sec;
        tmcell.tv_usec = tv00.tv_usec;
        cellvector.push_back(tmcell);
    }
    printf("=======\n");
    gettimeofday(&tv0, NULL);
    sum1 = 0;
    for (iter = cellvector.begin(); iter != cellvector.end(); ++iter) {
        if (!(iter->tv_sec % 5 || iter->tv_usec % 5))
            sum1++;
    }
    printf("sum1 %d\n", sum1);

    gettimeofday(&tv1, NULL);
    sum0 = 0;
    for (idx = 0; idx < 10000000; ++idx){
        if (!(cellvector[idx].tv_sec % 5 || cellvector[idx].tv_usec % 5))
            sum0++;
    }
    printf("sum0 %d\n", sum0);
    gettimeofday(&tv2, NULL);
    diff0 = tvdiff(tv1, tv0);
    diff1 = tvdiff(tv2, tv1);
    printf("%u, %u, %6.4f\n", diff1, diff0, (double)diff0/diff1);
    getchar();
    return 0;
}
