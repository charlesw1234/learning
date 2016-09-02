#include "freeze.hpp"
#include "freezerender.hpp"
#include <stdio.h>

#define SHOWSZ2(TYPE1, TYPE2) \
    printf("sizeof(%s) = %u, sizeof(%s) = %u\n", \
           #TYPE1, (unsigned)sizeof(TYPE1), #TYPE2, (unsigned)sizeof(TYPE2))

int main(void)
{
    SHOWSZ2(fjson::header_t, unsigned);
    SHOWSZ2(fjson::value4_t, fjson::value8_t);
    SHOWSZ2(fjson::Document4_t, fjson::Document8_t);
    SHOWSZ2(fjson::Render4_t, fjson::Render8_t);
    SHOWSZ2(fjson::DocumentAuto_t, unsigned);
}
