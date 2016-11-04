#include "flatten.hpp"

int main(void)
{
    flatten::storage_t storage;
    storage.push_back(flatten::space_t());
    printf("sizeof(flatten::flatten_size_t) = %u\n", (unsigned)sizeof(flatten::flatten_size_t));
    return 0;
}
