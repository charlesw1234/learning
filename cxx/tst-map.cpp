#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

class value_t
{
};
class ValueMap_t: public std::map<std::string, value_t *>
{
public:
    virtual ~ValueMap_t();
};
ValueMap_t::~ValueMap_t()
{
    ValueMap_t::const_iterator iter;
    for (iter = begin(); iter != end(); ++iter)
	delete iter->second;
}

int
main(int argc, char *argv[])
{
    ValueMap_t *vmap;
    ValueMap_t::const_iterator iter;

    vmap = new ValueMap_t();
    (*vmap)["yes"] = new value_t();
    (*vmap)["no"] = new value_t();
    for (iter = vmap->begin(); iter != vmap->end(); ++iter)
	printf("[%s]: %p\n", iter->first.c_str(), iter->second);
    delete vmap;
    return 0;
}
