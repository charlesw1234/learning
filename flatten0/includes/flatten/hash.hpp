#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class HASH_NODE_T>
    class hash_t: public segment_t<SIZE_T> {
    public:
        inline hash_t(size_t hashsize): segment_t<SIZE_T>(0, hashsize * sizeof(HASH_NODE_T)) {}
    };

    template<typename SIZE_T>
    class hash_list_body_t {
    };
}
