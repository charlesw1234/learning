#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    template<size_t NODESIZE>class hashes_t: public nodes_t<NODESIZE> {
    public:
        hashes_t(size_t step);
        hashes_t<NODESIZE> *flatten(void) const; // merge the delta to build a new hashes_t.
    };
}
