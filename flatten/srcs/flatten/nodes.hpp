#pragma once

#include "flatten/defs.hpp"

namespace flatten {
    template<int NODESIZE>class nodes_t {
    public:
        nodes_t(void) { head = tail = NULL; }
        inline size_t numnodes(void) const { return (tail - head) / NODESIZE; }
    private:
        uint8_t *head, *tail;
    };
}
