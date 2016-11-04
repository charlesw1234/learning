#include "flatten.hpp"

#define SHOWSZ(TYPE) printf("sizeof(%s) = %u\n", #TYPE, (unsigned)sizeof(TYPE))
#define SHOWSZ2(TYPE0, TYPE1)						\
    printf("sizeof(%s) = %u, sizeof(%s) = %u\n",			\
	   #TYPE0, (unsigned)sizeof(TYPE0), #TYPE1, (unsigned)sizeof(TYPE1))

int main(void)
{
    SHOWSZ2(int8_t, uint8_t);
    SHOWSZ2(int16_t, uint16_t);
    SHOWSZ2(int32_t, uint32_t);
    SHOWSZ2(int64_t, uint64_t);
    SHOWSZ2(char, unsigned char);
    SHOWSZ2(short, unsigned short);
    SHOWSZ2(int, unsigned);
    SHOWSZ2(long, unsigned long);
    SHOWSZ2(long long, unsigned long long);
    SHOWSZ2(float, double);
    SHOWSZ2(void *, size_t);
    SHOWSZ(flatten::f_size_t);
    SHOWSZ2(flatten::space_t, flatten::storage_t);
    return 0;
}
