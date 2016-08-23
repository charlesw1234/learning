#include "rapidjson/filereadstream.h"
#include "freezecmp.cpp"

int main(void)
{
    char buffer[4096];
    rapidjson::Document doc;
    FILE *rfp = fopen("config.json", "r");
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    fclose(rfp);

    fjson::Document8_t fdoc80(&doc);
    fjson::Document4_t fdoc40(&doc);
    printf("cmp_rf8 = %s, cmp_rf4 = %s\n",
           recur_cmp_rf<fjson::Document8_t>(&doc, &fdoc80, 0) ? "true": "false",
           recur_cmp_rf<fjson::Document4_t>(&doc, &fdoc40, 0) ? "true": "false");

    uint32_t pos8 = fdoc80.Locate(0, "syncdata");
    uint32_t pos4 = fdoc40.Locate(0, "syncdata");
    fjson::Document8_t fdoc81(&fdoc80, pos8);
    fjson::Document4_t fdoc41(&fdoc40, pos4);
    printf("cmp_f8f8 = %s, cmp_f4f4 = %s\n",
           recur_cmp_ff<fjson::Document8_t>(&fdoc80, pos8, &fdoc81, 0) ? "true": "false",
           recur_cmp_ff<fjson::Document4_t>(&fdoc40, pos4, &fdoc41, 0) ? "true": "false");
    printf("body8_size = %u, %u\n", (uint32_t)fdoc80.BodySize(), (uint32_t)fdoc81.BodySize());
    printf("body4_size = %u, %u\n", (uint32_t)fdoc40.BodySize(), (uint32_t)fdoc41.BodySize());
    return 0;
}
