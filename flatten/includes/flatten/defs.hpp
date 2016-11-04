#pragma once

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>

namespace flatten {
#if FLATTEN_SIZE == 1
    static const size_t size_bits = 8;
    typedef uint8_t flatten_size_t;
#elif FLATTEN_SIZE == 2
    static const size_t size_bits = 16;
    typedef uint16_t flatten_size_t;
#elif FLATTEN_SIZE == 4
    static const size_t size_bits = 32;
    typedef uint32_t flatten_size_t;
#elif FLATTEN_SIZE == 8
    static const size_t size_bits = 64;
    typedef uint64_t flatten_size_t;
#endif
}
