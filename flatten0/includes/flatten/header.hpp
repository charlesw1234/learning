#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class HEADER_BODY_T>
    class header_t: public segment_t<SIZE_T> {
    public:
        inline header_t(void): segment_t<SIZE_T>(0, sizeof(HEADER_BODY_T)) {}
    };
}
