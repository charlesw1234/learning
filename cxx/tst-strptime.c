#define _XOPEN_SOURCE
#include <stdio.h>
#include <string.h>
#include <time.h>

void
showtm(const char *prefix, const struct tm *tm)
{
    printf("%s: %d-%02d-%02d %02d:%02d:%02d wday(%d), yday(%d), isdst(%d)\n",
	   prefix, 1900 + tm->tm_year, tm->tm_mon, tm->tm_mday,
	   tm->tm_hour, tm->tm_min, tm->tm_sec,
	   tm->tm_wday, tm->tm_yday, tm->tm_isdst);
}

int
main(int argc, char *argv[])
{
    struct tm tm;
    memset(&tm, 0, sizeof(tm));
    strptime(argv[1], argv[2], &tm);
    showtm("strptime", &tm);
    return 0;
}
