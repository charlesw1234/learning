#include <typeinfo>
#include "rapidjson/document.h"

int
main(void)
{
    rapidjson::Document doc0(rapidjson::kObjectType);
    rapidjson::Document *doc1 = new rapidjson::Document(rapidjson::kObjectType);
    doc0.AddMember("first", rapidjson::Value(128), doc0.GetAllocator());
    doc0.AddMember("second", rapidjson::Value(), doc0.GetAllocator());
    printf("doc0 = %p, allocator = %s\n", &doc0, typeid(doc0.GetAllocator()).name());
    printf("doc0[first] = %p, doc1[second] = %p\n", &doc0["first"], &doc0["second"]);
    printf("doc1 = %p, allocator = %s\n", doc1, typeid(doc1->GetAllocator()).name());
    return 0;
}
