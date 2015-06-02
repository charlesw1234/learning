#include <stdio.h>

int
main(void)
{
    double dv1 = 8.88, dv2 = 8.875, dv3 = ((int)(dv2 * 100 + 0.5)) / 100.0;
    printf("%f, %f, %f, %s\n", dv1, dv2, dv3, dv1 == dv3 ? "true": "false");
    return 0;
}
