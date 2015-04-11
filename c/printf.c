#include <stdio.h>

int
main(void)
{
    fprintf(stderr, "%1$u: %2$s, %3$s, %2$s\n", __LINE__, "first", "second");
    fprintf(stderr, "%1$u: %3$s, %2$s\n", __LINE__, "first", "second");
    fprintf(stderr, "%1$u: %3$s\n", __LINE__, "first", "second");
    return 0;
}
