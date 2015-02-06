#include <stdio.h>
#include <bitset>

int main(void)
{
    std::bitset<8> bs0;
    std::bitset<64> bs1;
    std::bitset<65> bs2;
    printf("sizeof(bs0) = %u, bs0 = 0x%lX\n",
           (unsigned)sizeof(bs0), bs0.to_ulong());
    printf("sizeof(bs1) = %u, bs1 = 0x%lX\n",
           (unsigned)sizeof(bs1), bs1.to_ulong());
    printf("sizeof(bs2) = %u, bs2 = 0x%lX\n",
           (unsigned)sizeof(bs2), bs2.to_ulong());
    return 0;
}
