#pragma once

#include "globals.hpp"

namespace density {
    class memory_location_t {
    public:
        uint8_t *pointer;
        uint_fast64_t available_bytes;
        uint_fast64_t initial_available_bytes;

        inline void encapsulate(uint8_t *RESTRICT pointer, const uint_fast64_t bytes) {
            this->pointer = pointer;
            available_bytes = bytes;
            initial_available_bytes = bytes;
        }
        inline uint_fast64_t used(void) const
        {   return initial_available_bytes - available_bytes; }
    };
}
