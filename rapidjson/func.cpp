#include "show.hpp"

class container_t {
public:
    rapidjson::Value mValue;
    inline void set(rapidjson::Value &value)
    {
        printf("%u: mValue = %s, value = %s\n", __LINE__,
               shvalue(&mValue).c_str(), shvalue(&value).c_str());
        mValue = value;
        printf("%u: mValue = %s, value = %s\n", __LINE__,
               shvalue(&mValue).c_str(), shvalue(&value).c_str());
    }
};

int
main(void)
{
    container_t container;
    rapidjson::Document doc(rapidjson::kObjectType);
    rapidjson::Value arr0(rapidjson::kArrayType);
    rapidjson::Value ele0(128);
    rapidjson::Value ele1("128");
    arr0.PushBack(ele0, doc.GetAllocator());
    arr0.PushBack(ele1, doc.GetAllocator());
    doc.AddMember("first", arr0, doc.GetAllocator());

    printf("arr0: %s\n", shvalue(&arr0).c_str());
    printf("ele0: %s\n", shvalue(&ele0).c_str());
    printf("ele1: %s\n", shvalue(&ele1).c_str());
    printf("%s\n", shvalue(&doc).c_str());
    shobject(stdout, 4, doc);

    printf("----\n");
    container.set(doc["first"]);
    printf("%s\n", shvalue(&doc).c_str());
    shobject(stdout, 4, doc);
    return 0;
}
