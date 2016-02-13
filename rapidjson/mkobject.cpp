#include "rapidjson/writer.h"
#include "rapidjson/document.h"
#include "rapidjson/filewritestream.h"

int main(void)
{
    rapidjson::Document doc(rapidjson::kObjectType);
    rapidjson::Value subobj(rapidjson::kObjectType);
    doc.AddMember("first", 128, doc.GetAllocator());
    doc.AddMember("second", true, doc.GetAllocator());
    subobj.AddMember("third", "something", doc.GetAllocator());
    doc.AddMember("forth", subobj, doc.GetAllocator());
    FILE *wfp = fopen("mkobject.json", "wt");
    char buffer[4096];
    rapidjson::FileWriteStream fstrm(wfp, buffer, sizeof(buffer));
    rapidjson::Writer<rapidjson::FileWriteStream> writer(fstrm);
    doc.Accept(writer);
    fclose(wfp);
    return 0;
}
