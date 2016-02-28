#include <stdio.h>
#include <typeinfo>

class a_t {
public:
    unsigned avalue;
    //a_t(void) { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
    //~a_t() { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
};
class b_t {
public:
    double bvalue;
    //b_t(void) { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
    //~b_t() { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
};
class c_t {
public:
    union {
        a_t aobj;
        b_t bobj;
    } u;
    c_t(void) { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
    ~c_t() { printf("%s(%p)::%s\n", typeid(*this).name(), this, __FUNCTION__); }
};

int
main(void)
{
    c_t cobj;
    printf("sizeof(cobj) = %u\n", (unsigned)sizeof(cobj));
    printf("sizeof(cobj.u.aobj) = %u\n", (unsigned)sizeof(cobj.u.aobj));
    printf("sizeof(cobj.u.bobj) = %u\n", (unsigned)sizeof(cobj.u.bobj));
    return 0;
}
