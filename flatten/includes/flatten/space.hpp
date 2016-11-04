#pragma once

#include "flatten/segment.hpp"

namespace flatten {
    class space_t {
    public:
        inline space_t(void): _space(NULL), _free(NULL) {}
        inline ~space_t() { if (_free) free(_free); }

        flatten_size_t base(void) const;
        flatten_size_t size(void) const;
        void setbase(flatten_size_t base);
        bool save(file_t *file) const;
        bool save(memfile_t *file) const;
    private:
        uint8_t *_space, *_free;
#ifndef FLATTEN_MULTI_SIZE
        segment_t<flatten_size_t> *_segment;
#else
        uint8_t _size;
        union {
            segment_t<uint8_t> *u1;
            segment_t<uint16_t> *u2;
            segment_t<uint32_t> *u4;
            segment_t<uint64_t> *u8;
        } _segment;
#define FLATTEN_MULTI_SWITCH(STATE) switch (_size) { \
        case 1: return _segment.u1->STATE;           \
        case 2: return _segment.u2->STATE;           \
        case 4: return _segment.u4->STATE;           \
        case 8: return _segment.u8->STATE;           \
        }
#endif
    };

#ifndef FLATTEN_MULTI_SIZE
    inline flatten_size_t space_t::base(void) const { return _segment->base(); }
    inline flatten_size_t space_t::size(void) const { return _segment->size(); }
    inline void space_t::setbase(flatten_size_t base) { _segment->setbase(base); }
    inline bool space_t::save(file_t *file) const { _segment->save(file, _space); }
    inline bool space_t::save(memfile_t *file) const { _segment->save(file, _space); }
#else
    inline flatten_size_t space_t::base(void) const
    {   FLATTEN_MULTI_SWITCH(base()); return 0; }
    inline flatten_size_t space_t::size(void) const
    {   FLATTEN_MULTI_SWITCH(size()); return 0; }
    inline void space_t::setbase(flatten_size_t base) { FLATTEN_MULTI_SWITCH(setbase(base)); }
    inline bool space_t::save(file_t *file) const
    {   FLATTEN_MULTI_SWITCH(save(file, _space)); return false; }
    inline bool space_t::save(memfile_t *file) const
    {   FLATTEN_MULTI_SWITCH(save(file, _space)); return false; }
#endif
}
