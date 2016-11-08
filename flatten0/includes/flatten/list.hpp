#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class LIST_HEADER_T, class LIST_BODY_T>
    class list_t: public segment_t<SIZE_T> {
    public:
        inline list_t(void):
            segment_t<SIZE_T>(0, sizeof(LIST_HEADER_T) + sizeof(LIST_BODY_T)) {}
    };
}
