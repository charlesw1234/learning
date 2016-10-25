#pragma once

namespace flatten {
    class block_t {
    };
    class strings_t: public block_t {
    };
    template<class NODE_T> class array_t: public block_t {
    };
    template<class NODE_T> class arrays_t: public block_t {
    };
    template<class NODE_T> class hash_t: public block_t {
    };
    template<class NODE_T> class hashes_t: public block_t {
    };
}
