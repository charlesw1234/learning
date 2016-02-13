#include <typeinfo>
#include "show.hpp"

static void
add_on_ref(rapidjson::Value &refvalue, rapidjson::Document::AllocatorType &allocator)
{
    rapidjson::Value subarr(rapidjson::kArrayType);
    rapidjson::Value ele0(128);
    rapidjson::Value ele1("128");
    subarr.PushBack(ele0, allocator);
    subarr.PushBack(ele1, allocator);
    refvalue.AddMember("first", subarr, allocator);
    printf("ele0: %s\n", shvalue(&ele0).c_str());
    printf("ele1: %s\n", shvalue(&ele1).c_str());
    printf("subarr: %s\n", shvalue(&subarr).c_str());
}
static void
add_on_ptr(rapidjson::Value *ptrvalue, rapidjson::Document::AllocatorType &allocator)
{
    rapidjson::Value *ele0 = new rapidjson::Value(128);
    rapidjson::Value *ele1 = new rapidjson::Value("128");
    rapidjson::Value *subarr = new rapidjson::Value(rapidjson::kArrayType);
    subarr->PushBack(*ele0, allocator);
    subarr->PushBack(*ele1, allocator);
    ptrvalue->AddMember("first", *subarr, allocator);
    printf("ele0: %s\n", shvalue(ele0).c_str());
    printf("ele1: %s\n", shvalue(ele1).c_str());
    printf("subarr: %s\n", shvalue(subarr).c_str());
}

int
main(void)
{
    rapidjson::Document doc0(rapidjson::kObjectType);
    rapidjson::Document *doc1 = new rapidjson::Document(rapidjson::kObjectType);
    printf("doc0 = %p, allocator = %s\n", &doc0, typeid(doc0.GetAllocator()).name());
    add_on_ref(doc0, doc0.GetAllocator());
    printf("%s\n", shvalue(&doc0).c_str());
    shobject(stdout, 4, doc0);
    printf("\n");
    printf("doc1 = %p, allocator = %s\n", doc1, typeid(doc1->GetAllocator()).name());
    add_on_ptr(doc1, doc1->GetAllocator());
    printf("%s\n", shvalue(doc1).c_str());
    shobject(stdout, 4, *doc1);
    printf("\n");
    printf("doc0 %s doc1\n", doc0 == *doc1 ? "==": "!=");
    printf("doc0[first] %s doc1[first]\n", doc0["first"] == (*doc1)["first"] ? "==": "!=");
    delete doc1;
    return 0;
}
