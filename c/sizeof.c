#include <stdio.h>

#define SHSIZEOF(TYPE)  printf("sizeof(%s) = %u\n", #TYPE, (unsigned)sizeof(TYPE))

int
main(void)
{
    SHSIZEOF(int);
    SHSIZEOF(long);
    SHSIZEOF(long long);
    SHSIZEOF(unsigned);
    SHSIZEOF(unsigned long);
    SHSIZEOF(unsigned long long);
    SHSIZEOF(float);
    SHSIZEOF(double);
    return 0;
}
