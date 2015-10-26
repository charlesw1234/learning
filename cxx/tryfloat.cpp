#include <stdio.h>

int
main(void)
{
    float fval0 = 3550.001;
    float fval1 = 3550.003;
    float fval2 = 0.02;
    printf("%f, %f, %f, %f\n", fval0, fval1, fval2, fval1 - fval0);
    return 0;
}
