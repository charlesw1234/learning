#pragma once

#include "flatten/defs.hpp"

namespace flatten {
    class space_exception {};

    template<typename SIZE_T>class segment_t {
    public:
        static bool comp(const segment_t &segment0, const segment_t &segment1)
        {   return segment0._base < segment1._base; }

        inline segment_t(SIZE_T base, SIZE_T size):
            _base(base), _size(size), _space(NULL), _free(NULL) {}
        inline ~segment_t() { if (_free) free(_free); }

        inline SIZE_T base(void) const { return _base; }
        inline SIZE_T size(void) const { return _size; }

        template<typename SIZE0_T>
        inline const uint8_t *load_base(const uint8_t *cur, const uint8_t *last)
        {   //if (cur + sizeof(SIZE0_T) > last) throw space_exception();
            _base = *(const SIZE0_T *)cur; return cur + sizeof(SIZE0_T); }
        template<typename SIZE1_T>
        inline const uint8_t *load_size(const uint8_t *cur, const uint8_t *last)
        {   //if (cur + sizeof(SIZE1_T) > last) throw space_exception();
            _size = *(const SIZE1_T *)cur; return cur + sizeof(SIZE1_T); }
        template<typename SIZE0_T, typename SIZE1_T>
        inline const uint8_t *load(const uint8_t *cur, const uint8_t *last)
        {   return load_size<SIZE1_T>(load_base<SIZE0_T>(cur, last), last); }

        template<typename SIZE0_T>
        inline uint8_t *save_base(uint8_t *cur, uint8_t *last)
        {   //if (cur + sizeof(SIZE0_T) > last) throw space_exception();
            *(SIZE0_T *)cur = _base; return cur + sizeof(SIZE0_T); }
        template<typename SIZE1_T>
        inline uint8_t *save_size(uint8_t *cur, uint8_t *last)
        {   //if (cur + sizeof(SIZE1_T) > last) throw space_exception();
            *(SIZE1_T *)cur = _size; return cur + sizeof(SIZE1_T); }
        template<typename SIZE0_T, typename SIZE1_T>
        inline uint8_t *save(uint8_t *cur, uint8_t *last)
        {   return save_size<SIZE1_T>(save_base<SIZE0_T>(cur, last), last); }
    private:
        SIZE_T _base, _size;
        uint8_t *_space, *_free;
    };
}
