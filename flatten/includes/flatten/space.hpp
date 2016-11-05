#pragma once

#include "flatten/segment.hpp"

namespace flatten {
#define FLATTEN_SWITCH(STATE, VALUE) switch (_size) {   \
        case 1: return _segment.u1->STATE;           \
        case 2: return _segment.u2->STATE;           \
        case 4: return _segment.u4->STATE;           \
        case 8: return _segment.u8->STATE;           \
        }       return VALUE

    template<typename SIZE_T>class space_t {
    public:
         inline space_t(void): _space(NULL), _free(NULL) {}
        inline ~space_t() { if (_free) free(_free); }

        inline SIZE_T base(void) const { return _segment->u0.base(); }
        inline SIZE_T mbase(void) const { FLATTEN_SWITCH(base(), 0); }

        inline SIZE_T size(void) const { return _segment->u0.size(); }
        inline SIZE_T msize(void) const { FLATTEN_SWITCH(size(), 0); }

        inline void setbase(SIZE_T base) { return _segment->u0.setbase(base); }
        inline void msetbase(SIZE_T base) { FLATTEN_SWITCH(setbase(base),); }
        inline void setsize(SIZE_T size) { return _segment->u0.setsize(size); }
        inline void msetsize(SIZE_T size) { FLATTEN_SWITCH(setbase(base),); }

        inline bool load(file_t *file) { return _segment->u0.load(file, _space); }
        inline bool mload(file_t *file) { FLATTEN_SWITCH(load(file, _space), false); }
        inline bool load(memfile_t *file) { return _segment->u0.load(file, _space); }
        inline bool mload(memfile_t *file) { FLATTEN_SWITCH(load(file, _space), false); }
        inline bool save(file_t *file) const { return _segment->u0.save(file, _space); }
        inline bool msave(file_t *file) const { FLATTEN_SWITCH(save(file, _space), false); }
        inline bool save(memfile_t *file) const { return _segment->u0.save(file, _space); }
        inline bool msave(memfile_t *file) const { FLATTEN_SWITCH(save(file, _space), false); }
    private:
        bool _dirty;
        uint8_t _size;
        uint8_t *_space, *_free;
        union {
            segment_t<SIZE_T> *u0;
            segment_t<uint8_t> *u1;
            segment_t<uint16_t> *u2;
            segment_t<uint32_t> *u4;
            segment_t<uint64_t> *u8;
        }   _segment;
    };
}
