#include <time.h>

double myvar = 3.0;

int fact(int n)
{   return n <= 1 ? 1: n * fact(n - 1); }

int my_mod(int x, int y)
{   return x % y; }

char *get_time(void)
{
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);
}
