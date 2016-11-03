#pragma once

#include "flatten/space.hpp"

namespace flatten {
    class storage_t: public std::vector<space_t> {
    public:
	inline storage_t(void): std::vector<space_t>() {}
	inline ~storage_t() {}

#define FLATTEN_STORAGE_REBASE(SIZE, SIZE_T)                            \
	inline void rebase##SIZE(SIZE_T curbase = 0)                    \
	{   for (size_t idx = 0; idx < size(); ++idx) {                 \
                at(idx).setbase##SIZE(curbase); curbase += at(idx).size(); } }

        FLATTEN_STORAGE_REBASE(8, uint8_t);
        FLATTEN_STORAGE_REBASE(16, uint16_t);
        FLATTEN_STORAGE_REBASE(32, uint32_t);
        FLATTEN_STORAGE_REBASE(64, uint64_t);
#ifdef FLATTEN_MULTI_SIZE
        FLATTEN_STORAGE_REBASE(, FLATTEN_MAXSIZE_T);
#endif

#define FLATTEN_STORAGE_SAVE(SIZE)                                      \
        inline void save##SIZE(file_t *file)                            \
        {   for (size_t idx = 0; idx < size(); ++idx) at(idx).save##SIZE(file); } \
        inline void save##SIZE(memfile_t *file)                         \
        {   for (size_t idx = 0; idx < size(); ++idx) at(idx).save##SIZE(file); }

        FLATTEN_STORAGE_SAVE(8);
        FLATTEN_STORAGE_SAVE(16);
        FLATTEN_STORAGE_SAVE(32);
        FLATTEN_STORAGE_SAVE(64);
#ifdef FLATTEN_MULTI_SIZE
        FLATTEN_STORAGE_SAVE();
#endif
    };
}
