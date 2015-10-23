#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

enum NumberType_t { NumberDouble, NumberInt, NumberUInt };
enum NumberPrecision_t { NumberCommon, Number10000, Number100000 };

class Number0_t {
private:
    bool _decimal;
    bool _negative;
    union {
        int64_t value;
        uint64_t uvalue;
        double dvalue;
    } _u;
};
class Number1_t {
private:
    NumberType_t _type;
    union {
        int64_t value;
        uint64_t uvalue;
        double dvalue;
    } _u;
};
class Number2_t {
private:
    NumberType_t _type;
    NumberPrecision_t _precision;
    union {
        int64_t value;
        uint64_t uvalue;
        double dvalue;
    } _u;
};

int
main(void)
{
    uint8_t byte;
    uint8_t *pbyte0 = &byte, *pbyte1 = NULL;
    ptrdiff_t val = pbyte0 - pbyte1;
    printf("sizeof(Number0_t) = %u\n", (unsigned)sizeof(Number0_t));
    printf("sizeof(Number1_t) = %u\n", (unsigned)sizeof(Number1_t));
    printf("sizeof(Number2_t) = %u\n", (unsigned)sizeof(Number2_t));
#define SHOWSZ(TYPE) printf("sizeof(" #TYPE ") = %u\n", (unsigned)sizeof(TYPE))
    SHOWSZ(short);
    SHOWSZ(unsigned short);
    SHOWSZ(int);
    SHOWSZ(unsigned);
    SHOWSZ(long);
    SHOWSZ(unsigned long);
    SHOWSZ(long long);
    SHOWSZ(unsigned long long);
    SHOWSZ(float);
    SHOWSZ(double);
    SHOWSZ(void *);
    SHOWSZ(ptrdiff_t);
    printf("val = %lx, %p, %p\n", (unsigned long)val, pbyte0, pbyte1);
    return 0;
}
