#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    template<size_t NODESIZE>class arrays_t: public nodes_t<NODESIZE> {
    public:
        arrays_t(void);
        arrays_t<NODESIZE> *flatten(void) const; // merge the delta to build a new arrays_t.
    };
}
