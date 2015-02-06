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
    printf("sizeof(Number0_t) = %u\n", (unsigned)sizeof(Number0_t));
    printf("sizeof(Number1_t) = %u\n", (unsigned)sizeof(Number1_t));
    printf("sizeof(Number2_t) = %u\n", (unsigned)sizeof(Number2_t));
    return 0;
}
