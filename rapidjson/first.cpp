#include "show.hpp"
#include "rapidjson/filereadstream.h"

int main(void)
{
    char buffer[4096];
    rapidjson::Document doc;
    FILE *rfp = fopen("config.json", "r");
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    printf("%s\n", shvalue(&doc).c_str());
    shobject(stdout, 4, doc);
    fclose(rfp);
    return 0;
}
