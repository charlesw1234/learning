#include <stdio.h>

class Class_t {
public:
    int value;
    inline Class_t(void) { value = 0; printf("%s(%u)\n", __FUNCTION__, __LINE__); }
    inline ~Class_t() { printf("%s(%u)\n", __FUNCTION__, __LINE__); }
};

class ClassContainer_t {
public:
    int type;
    union {
        Class_t cobj0;
        Class_t cobj1;
    } ucs;
};

int main(void)
{
    ClassContainer_t container;
    return 0;
}
