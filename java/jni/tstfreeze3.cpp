#include "rapidjson/filereadstream.h"
#include "freeze.hpp"

int main(void)
{
    char buffer[8192];
    rapidjson::Document doc;
    FILE *rfp = fopen("prompts_1_2.json", "r");
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    fclose(rfp);

    fjson::Document8_t fdoc(&doc);
    printf("ValueSize = %u, BodySize = %u\n",
           (unsigned)fdoc.ValueSize(), (unsigned)fdoc.BodySize());
    return 0;
}
