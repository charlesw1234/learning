#include <stdio.h>

static unsigned primes[1024] = { 2, 3, 5, 7, 11, 13, 17, 19 };
static unsigned *primes_cur = primes + 8;
static unsigned *primes_last = primes + sizeof(primes) / sizeof(primes[0]);

static int
check_prime(unsigned value)
{
    unsigned *primes_cur0;
    for (primes_cur0 = primes; primes_cur0 < primes_cur; ++primes_cur0)
        if (value % *primes_cur0 == 0) return 0;
        else if (*primes_cur0 * *primes_cur0 > value) return 1;
    return 1;
}

int main(void)
{
    unsigned value, last, idx, idx0;
    while (primes_cur < primes_last) {
        last = primes_cur[-1];
        for (value = last + 2; value < last * last; value += 2) {
            if (!check_prime(value)) continue;
            *primes_cur++ = value;
            break;
        }
    }
    printf("const unsigned primes[] = {\n");
    for (idx = 0; idx < primes_last - primes; idx += 16) {
        printf("    ");
        for (idx0 = 0; idx0 < 16; ++idx0)
            printf("%u, ", primes[idx + idx0]);
        printf("\n");
    }
    printf("};\n");
    return 0;
}
