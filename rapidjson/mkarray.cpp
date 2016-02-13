#include "rapidjson/writer.h"
#include "rapidjson/document.h"
#include "rapidjson/filewritestream.h"

int main(void)
{
    rapidjson::Document doc(rapidjson::kArrayType);
    rapidjson::Value subarr(rapidjson::kArrayType);
    doc.PushBack("literal", doc.GetAllocator());
    doc.PushBack(128, doc.GetAllocator());
    subarr.PushBack("first", doc.GetAllocator()).PushBack("second", doc.GetAllocator());
    doc.PushBack(subarr, doc.GetAllocator());
    FILE *wfp = fopen("mkarray.json", "wt");
    char buffer[4096];
    rapidjson::FileWriteStream fstrm(wfp, buffer, sizeof(buffer));
    rapidjson::Writer<rapidjson::FileWriteStream> writer(fstrm);
    doc.Accept(writer);
    fclose(wfp);
    return 0;
}
