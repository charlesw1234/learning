#include "flatten.hpp"

class header_t: public flatten::space_t<uint8_t> {
public:
    inline header_t(void)
    {   _dirty = false; _size = _sbody.sizeof_size(), _space = (uint8_t *)&_body; _free = NULL;
        _sbody.setbase(0); _sbody.setsize(sizeof(_body)); }

    inline void setup(void)
    {   _body.magic = 0xAABBCCDD;
        _body.hash_size = 11; _body.hash_steps = 3;
        _body.padding = 0; _body.unused = 0; }
private:
    flatten::segment_t<uint8_t> _sbody;
    struct {
        uint32_t magic;
        uint16_t hash_size;
        uint8_t  hash_steps;
        uint8_t  padding;
        uint64_t unused;
    }  _body;
};

int main(void)
{
    flatten::memfile_t(4096);
    flatten::storage_t<uint32_t> storage;
    storage.push_back(flatten::space_t<uint32_t>());
    std::sort(storage.begin(), storage.end(), flatten::space_t<uint32_t>::comp);
    return 0;
}
