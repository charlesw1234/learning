#include <stdint.h>
#include <stdio.h>

template<typename TYPE> class temp_t {
public:
    TYPE *obj;
};

class myclass_t: public temp_t<myclass_t> {
public:
    uint32_t value1;
};

int
main(void)
{
    myclass_t myobj;
    printf("sizeof(myobj) = %u\n", (unsigned)sizeof(myobj));
    return 0;
}
