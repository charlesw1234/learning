#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    template<size_t NODESIZE>class array_t: public nodes_t<NODESIZE> {
    public:
        array_t(void);
        array_t<NODESIZE> *flatten(void) const; // merge the delta to build a new array_t.
    };
}
