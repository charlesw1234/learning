#include "rapidjson/document.h"

#define SHOWSZ(TYPE)  printf("sizeof(%s) = %u\n", #TYPE, (unsigned)sizeof(TYPE));
int main(void)
{
    SHOWSZ(rapidjson::Value);
    SHOWSZ(rapidjson::Document);
    return 0;
}
