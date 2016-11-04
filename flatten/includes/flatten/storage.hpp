#pragma once

#include "flatten/space.hpp"

namespace flatten {
    class storage_t: public std::vector<space_t> {
    public:
	inline storage_t(void): std::vector<space_t>() {}
	inline ~storage_t() {}

        inline void rebase(f_size_t curbase = 0)
        {   for (size_t idx = 0; idx < size(); ++idx) {
                at(idx).setbase(curbase); curbase += at(idx).size(); } }

        inline void save(file_t *file)
        {   for (size_t idx = 0; idx < size(); ++idx) at(idx).save(file); }
        inline void save(memfile_t *file)
        {   for (size_t idx = 0; idx < size(); ++idx) at(idx).save(file); }
    };
}
