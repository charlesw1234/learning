#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    class bytes_t: public nodes_t<1> {
    public:
        bytes_t(void);
        bytes_t *flatten(void) const; // merge the delta to build a new bytes_t.
    };
    class strings_t: public bytes_t {
    public:
        inline strings_t(void): bytes_t() {}
        strings_t *flatten(void) const;
    };
}
