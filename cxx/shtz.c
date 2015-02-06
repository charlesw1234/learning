#include <stdio.h>
#include <time.h>

int
main(void)
{
    tzset();
    printf("tzname[0] = [%s]\n", tzname[0]);
    printf("tzname[1] = [%s]\n", tzname[1]);
    printf("timezone = %ld\n", timezone);
    printf("daylight = %d\n", daylight);
    return 0;
}
