#pragma once

#include "flatten/space.hpp"

namespace flatten {
    class header_t {
    public:
        inline header_t(uint32_t magic) { _magic = magic; }
        inline uint32_t magic(void) { return _magic; }
    private:
        uint32_t _magic;
    };
}
