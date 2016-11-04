#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    class space_t {
    public:
        inline space_t(void): _space(NULL), _free(NULL) {}
        inline ~space_t() { if (_free) free(_free); }

        f_size_t base(void) const;
        f_size_t size(void) const;
        void setbase(f_size_t base);
        void setsize(f_size_t base);

        bool load(file_t *file);
        bool load(memfile_t *file);
        bool save(file_t *file) const;
        bool save(memfile_t *file) const;
    private:
        uint8_t *_space, *_free;
#ifndef FLATTEN_MULTI_SIZE
        segment_t<f_size_t> *_segment;
#else
        uint8_t _size;
        union {
            segment_t<uint8_t> *u1;
            segment_t<uint16_t> *u2;
            segment_t<uint32_t> *u4;
            segment_t<uint64_t> *u8;
        } _segment;
#endif
    };

#ifndef FLATTEN_MULTI_SIZE
    inline f_size_t space_t::base(void) const { return _segment->base(); }
    inline f_size_t space_t::size(void) const { return _segment->size(); }
    inline void space_t::setbase(f_size_t base) { _segment->setbase(base); }
    inline void space_t::setsize(f_size_t size) { _segment->setsize(size); }
    inline bool space_t::load(file_t *file) { _segment->load(file, _space); }
    inline bool space_t::load(memfile_t *file) { _segment->load(file, _space); }
    inline bool space_t::save(file_t *file) const { _segment->save(file, _space); }
    inline bool space_t::save(memfile_t *file) const { _segment->save(file, _space); }
#else
#define FLATTEN_MULTI_SWITCH(STATE) switch (_size) { \
        case 1: return _segment.u1->STATE;           \
        case 2: return _segment.u2->STATE;           \
        case 4: return _segment.u4->STATE;           \
        case 8: return _segment.u8->STATE;           \
        }
#define FLATTEN_MULTI_SWITCH2(STATE, VALUE) FLATTEN_MULTI_SWITCH(STATE); return VALUE
    inline f_size_t space_t::base(void) const { FLATTEN_MULTI_SWITCH2(base(), 0); }
    inline f_size_t space_t::size(void) const { FLATTEN_MULTI_SWITCH2(size(), 0); }
    inline void space_t::setbase(f_size_t base) { FLATTEN_MULTI_SWITCH(setbase(base)); }
    inline void space_t::setsize(f_size_t size) { FLATTEN_MULTI_SWITCH(setsize(size)); }
    inline bool space_t::load(file_t *file)
    {   FLATTEN_MULTI_SWITCH2(load(file, _space), false); }
    inline bool space_t::load(memfile_t *file)
    {   FLATTEN_MULTI_SWITCH2(load(file, _space), false); }
    inline bool space_t::save(file_t *file) const
    {   FLATTEN_MULTI_SWITCH2(save(file, _space), false); }
    inline bool space_t::save(memfile_t *file) const
    {   FLATTEN_MULTI_SWITCH2(save(file, _space), false); }
#endif
}
