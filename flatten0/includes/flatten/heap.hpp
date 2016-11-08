#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class HEAP_NODE_T>
    class heap_t: public segment_t<SIZE_T> {
    public:
        inline heap_t(size_t heapsize): segment_t<SIZE_T>(0, heapsize * sizeof(HEAP_NODE_T)) {}
    };

    template<typename SIZE_T>
    class heap_list_body_t {
    };
}
