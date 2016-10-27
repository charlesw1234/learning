#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    template<size_t NODESIZE>class hash_t: public nodes_t<NODESIZE> {
    public:
        hash_t(size_t multi);
        hash_t<NODESIZE> *flatten(void) const; // merge the delta to build a new hash_t.
    };
}
