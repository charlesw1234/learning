#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#ifdef _WIN32
#include <Time.h>
#include <Windows.h>
#else
#include <sys/time.h>
#endif

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

#define TEST_SIZE 10000
#define TEST_STR "This is a test string"

typedef struct {
    std::string str;
} StdStrType_t;

typedef struct {
    char *str;
} CharPtrType_t;

typedef struct {
    char str[512];
} CharArrType_t;

int main(void)
{
    unsigned idx;
    struct timeval tv0, tv1, tv2;
    std::vector<StdStrType_t> strvec;
    std::vector<CharPtrType_t> ptrvec;
    std::vector<CharArrType_t> arrvec;

    gettimeofday(&tv0, NULL);
    strvec.resize(TEST_SIZE);
    for (idx = 0; idx < strvec.size(); idx++) {
        strvec[idx].str.assign(TEST_STR);
    }
    gettimeofday(&tv1, NULL);
    printf("std::string vector create %d\n", tvdiff(tv1, tv0));
    strvec.clear();
    gettimeofday(&tv2, NULL);
    printf("std::string vector destroy %d\n", tvdiff(tv2, tv1));

    gettimeofday(&tv0, NULL);
    ptrvec.resize(TEST_SIZE);
    for (idx = 0; idx < ptrvec.size(); idx++) {
        ptrvec[idx].str = (char*)malloc(strlen(TEST_STR));
        memcpy(ptrvec[idx].str, TEST_STR, strlen(TEST_STR));
    }
    gettimeofday(&tv1, NULL);
    printf("char* vector create %d\n", tvdiff(tv1, tv0));
    for (idx = 0; idx < ptrvec.size(); idx++) {
        free(ptrvec[idx].str);
    }
    ptrvec.clear();
    gettimeofday(&tv2, NULL);
    printf("char* vector destroy %d\n", tvdiff(tv2, tv1));

    gettimeofday(&tv0, NULL);
    arrvec.resize(TEST_SIZE);
    for (idx = 0; idx < arrvec.size(); idx++) {
        memcpy(arrvec[idx].str, TEST_STR, strlen(TEST_STR));
    }
    gettimeofday(&tv1, NULL);
    printf("char[] vector create %d\n", tvdiff(tv1, tv0));
    arrvec.clear();
    gettimeofday(&tv2, NULL);
    printf("char[] vector destroy %d\n", tvdiff(tv2, tv1));

    getchar();
    return 0;
}
