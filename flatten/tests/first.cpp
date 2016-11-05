#include "flatten.hpp"

int main(void)
{
    flatten::memfile_t(4096);
    flatten::storage_t<uint32_t> storage;
    storage.push_back(flatten::space_t<uint32_t>());
    std::sort(storage.begin(), storage.end(), flatten::space_t<uint32_t>::comp);
    return 0;
}
