#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class ARRAY_NODE_T>
    class array_t: public segment_t<SIZE_T> {
    public:
        inline array_t(size_t arraysize):
            segment_t<SIZE_T>(0, arraysize * sizeof(ARRAY_NODE_T)) {}
    };

    template<typename SIZE_T>
    class arary_list_body_t {
    };
}
