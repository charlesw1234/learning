#include "flatten.hpp"

#define SHOWSZ(TYPE) printf("sizeof(%s) = %u\n", #TYPE, (unsigned)sizeof(TYPE))
#define SHOWSZ2(TYPE0, TYPE1)						\
    printf("sizeof(%s) = %u, sizeof(%s) = %u\n",			\
	   #TYPE0, (unsigned)sizeof(TYPE0),                             \
           #TYPE1, (unsigned)sizeof(TYPE1))
#define SHOWSZ3(TYPE0, TYPE1, TYPE2)                                    \
    printf("sizeof(%s) = %u, sizeof(%s) = %u, sizeof(%s) = %u\n",       \
	   #TYPE0, (unsigned)sizeof(TYPE0),                             \
           #TYPE1, (unsigned)sizeof(TYPE1),                             \
           #TYPE2, (unsigned)sizeof(TYPE2))
#define SHOWSZ4(TYPE0, TYPE1, TYPE2, TYPE3)                             \
    printf("sizeof(%s) = %u, sizeof(%s) = %u, sizeof(%s) = %u, sizeof(%s) = %u\n", \
	   #TYPE0, (unsigned)sizeof(TYPE0),                             \
           #TYPE1, (unsigned)sizeof(TYPE1),                             \
           #TYPE2, (unsigned)sizeof(TYPE2),                             \
           #TYPE3, (unsigned)sizeof(TYPE3))

int main(void)
{
    SHOWSZ4(int8_t, int16_t, int32_t, int64_t);
    SHOWSZ4(uint8_t, uint16_t, uint32_t, uint64_t);
    SHOWSZ4(short, int, long, long long);
    SHOWSZ4(unsigned short, unsigned, unsigned long, unsigned long long);
    SHOWSZ4(char, unsigned char, float, double);
    SHOWSZ2(void *, size_t);
    SHOWSZ2(flatten::file_t, flatten::memfile_t);
    SHOWSZ4(flatten::segment_t<uint8_t>,
            flatten::segment_t<uint16_t>,
            flatten::segment_t<uint32_t>,
            flatten::segment_t<uint64_t>);
    SHOWSZ4(flatten::space_t<uint8_t>,
            flatten::space_t<uint16_t>,
            flatten::space_t<uint32_t>,
            flatten::space_t<uint64_t>);
    SHOWSZ4(flatten::storage_t<uint8_t>,
            flatten::storage_t<uint16_t>,
            flatten::storage_t<uint32_t>,
            flatten::storage_t<uint64_t>);
    return 0;
}
