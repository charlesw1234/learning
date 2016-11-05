#pragma once

#include "flatten/space.hpp"

namespace flatten {
    template<typename SIZE_T>class storage_t: public std::vector<space_t<SIZE_T> > {
    private:
        SIZE_T _align;
        inline SIZE_T _do_align(SIZE_T size)
        {   SIZE_T remain = size % _align;
            return remain == 0 ? size: size + _align - remain; }
    public:
	inline storage_t(SIZE_T align = sizeof(SIZE_T)): std::vector<space_t<SIZE_T> >() {}
	inline ~storage_t() {}

        inline size_t size(void) const { return std::vector<space_t<SIZE_T> >::size(); }
        inline space_t<SIZE_T> &at(size_t idx)
        {   return std::vector<space_t<SIZE_T> >::at(idx); }
        inline const space_t<SIZE_T> &at(size_t idx) const
        {   return std::vector<space_t<SIZE_T> >::at(idx); }

        inline void rebase(SIZE_T curbase = 0)
        {   for (size_t idx = 0; idx < size(); ++idx) {
                at(idx).setbase(curbase); curbase += _do_align(at(idx).size()); } }

        inline bool save(file_t *file) const
        {   bool succ = true;
            for (size_t idx = 0; idx < size(); ++idx) succ = at(idx).save(file) && succ;
            return succ; }
        inline bool save(memfile_t *file) const
        {   bool succ = true;
            for (size_t idx = 0; idx < size(); ++idx) succ = at(idx).save(file) && succ;
            return succ; }
    };
}
