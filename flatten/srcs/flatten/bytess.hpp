#pragma once

#include "flatten/nodes.hpp"

namespace flatten {
    class bytess_t: public nodes_t<1> {
    public:
        bytess_t(void);
        bytess_t *flatten(void) const; // merge the delta to build a new bytess_t.
    };
    class stringss_t: public bytess_t {
    public:
        inline stringss_t(void): bytess_t() {}
        stringss_t *flatten(void) const;
    };
}
