#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    template<typename SIZE_T>
    class storage_t: std::vector<segment_t<SIZE_T> *> {
    public:
        inline storage_t(void): std::vector<segment_t<SIZE_T> *>() {}
        inline ~storage_t()
        {   for (size_t idx = 0; idx < size(); ++idx) delete at(idx); }
    };
}
