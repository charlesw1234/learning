#include <stdio.h>
#include "value.hpp"

#define SHOWSZ(TYPE) printf("sizeof(%s) = %u\n", #TYPE, (unsigned)sizeof(TYPE))
int
main(void)
{
    SHOWSZ(json::value_t);
    return 0;
}
