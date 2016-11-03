#pragma once

#include "flatten/storage.hpp"

namespace flatten {
    template<unsigned NODESIZE, typename SIZE_T>
    class nodes_t: public segment_t<SIZE_T> {
    public:
        nodes_t(void) {}
        inline SIZE_T numnodes(void) const { return size() / NODESIZE; }
    };
}
