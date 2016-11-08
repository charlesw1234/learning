#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T, class BYTE_NODE_T>
    class byte_t: public segment_t<SIZE_T> {
    public:
        inline byte_t(size_t bytesize): segment_t<SIZE_T>(0, bytesize * sizeof(BYTE_NODE_T)) {}
    };

    template<typename SIZE_T>
    class byte_list_body_t {
    };
}
