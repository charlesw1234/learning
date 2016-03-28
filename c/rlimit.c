#include <sys/time.h>
#include <sys/resource.h>
#include <stdio.h>

static void showit(int value, const char *name)
{
    struct rlimit rlim;
    if (getrlimit(value, &rlim) == 0)
        printf("%s: %llu, %llu\n", name,
               (unsigned long long)rlim.rlim_cur,
               (unsigned long long)rlim.rlim_max);
    else
        printf("%s: failed\n", name);
}
#define SHOWIT(RESOURCE)  showit(RESOURCE, #RESOURCE)
int main(void)
{
    SHOWIT(RLIMIT_AS);
    SHOWIT(RLIMIT_CORE);
    SHOWIT(RLIMIT_CPU);
    SHOWIT(RLIMIT_DATA);
    SHOWIT(RLIMIT_FSIZE);
    SHOWIT(RLIMIT_MEMLOCK);
    SHOWIT(RLIMIT_MSGQUEUE);
    SHOWIT(RLIMIT_MSGQUEUE);
    SHOWIT(RLIMIT_NICE);
    SHOWIT(RLIMIT_NOFILE);
    SHOWIT(RLIMIT_NPROC);
    SHOWIT(RLIMIT_RSS);
    SHOWIT(RLIMIT_RTPRIO);
    SHOWIT(RLIMIT_RTTIME);
    SHOWIT(RLIMIT_SIGPENDING);
    SHOWIT(RLIMIT_STACK);
    return 0;
}
