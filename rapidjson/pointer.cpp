#include "rapidjson/document.h"
#include "rapidjson/writer.h"

int main(void)
{
    rapidjson::Document *doc = new rapidjson::Document(rapidjson::kObjectType);
    rapidjson::Value subarr(rapidjson::kArrayType);
    doc->AddMember("tstarr", subarr, doc->GetAllocator());
    rapidjson::Value *subarrptr = &doc->FindMember("tstarr")->value;
    subarrptr->PushBack(128, doc->GetAllocator());
    subarrptr->PushBack(true, doc->GetAllocator());
    rapidjson::StringBuffer buffer;
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);
    doc->Accept(writer);
    printf("(%s)\n", buffer.GetString());
    delete doc;
    return 0;
}
