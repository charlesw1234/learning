#include <vector>
#include "rapidjson/document.h"

class container_t {
public:
    container_t(void) {}
    //virtual ~container_t() {}

    inline void setup(const std::string &name, const rapidjson::Value &value,
                      rapidjson::Document::AllocatorType &allocator)
    {   _name = name; _value.CopyFrom(value, allocator); }
private:
    std::string _name;
    rapidjson::Value _value;
};

class containers_t: public std::vector<container_t> {};

int
main(void)
{
    containers_t containers;
    containers.resize(5);
    return 0;
}
