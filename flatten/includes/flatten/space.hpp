#pragma once

#include "flatten/segment.hpp"

namespace flatten {
#ifdef FLATTEN_MULTI_SIZE
#define FLATTEN_MULTI_SWITCH(RETURN_T, FUNC, PROTOS, PARAMS, RETURN_DEFAULT) \
    inline RETURN_T FUNC PROTOS {                                       \
        switch (_size) {                                                \
        case 8: return FUNC##8 PARAMS;                                  \
        case 16: return FUNC##16 PARAMS;                                \
        case 32: return FUNC##32 PARAMS;                                \
        case 64: return FUNC##64 PARAMS;                                \
        }  return RETURN_DEFAULT; }
#else
#define FLATTEN_MULTI_SWITCH(RETURN_T, FUNC, PROTOS, PARAMS, RETURN_DEFAULT)
#endif

    class space_t {
    public:
        inline space_t(void): FLATTEN_MULTI_SIZE_ONLY(_size(16)), _space(NULL), _free(NULL) {}
        inline ~space_t() { if (_free) free(_free); }

        // size:
#define FLATTEN_SPACE_SIZE(SIZE)                \
        inline uint##SIZE##_t size##SIZE(void) const { return segment.u##SIZE->size(); }

        FLATTEN_SPACE_SIZE(8);
        FLATTEN_SPACE_SIZE(16);
        FLATTEN_SPACE_SIZE(32);
        FLATTEN_SPACE_SIZE(64);
        FLATTEN_MULTI_SWITCH(FLATTEN_MAXSIZE_T, size, (void) const, (), 0);

        // setbase:
#define FLATTEN_SPACE_SETBASE(SIZE)                                     \
        inline void setbase##SIZE(uint##SIZE##_t base) { segment.u##SIZE->setbase(base); }

        FLATTEN_SPACE_SETBASE(8);
        FLATTEN_SPACE_SETBASE(16);
        FLATTEN_SPACE_SETBASE(32);
        FLATTEN_SPACE_SETBASE(64);
        FLATTEN_MULTI_SWITCH(void, setbase, (FLATTEN_MAXSIZE_T base), (base),);

        // save:
#define FLATTEN_SPACE_SAVE( SIZE)                                       \
        inline bool save##SIZE(file_t *file) const                      \
        {   return segment.u##SIZE->save(file, _space); }               \
        inline bool save##SIZE(memfile_t *file) const                   \
        {   return segment.u##SIZE->save(file, _space); }

        FLATTEN_SPACE_SAVE(8);
        FLATTEN_SPACE_SAVE(16);
        FLATTEN_SPACE_SAVE(32);
        FLATTEN_SPACE_SAVE(64);
        FLATTEN_MULTI_SWITCH(bool, save, (file_t *file) const, (file), false)
        FLATTEN_MULTI_SWITCH(bool, save, (memfile_t *file) const, (file), false)
    private:
#ifdef FLATTEN_MULTI_SIZE
        uint8_t _size;
#endif
        uint8_t *_space, *_free;
        union {
            segment_t<uint8_t> *u8;
            segment_t<uint16_t> *u16;
            segment_t<uint32_t> *u32;
            segment_t<uint64_t> *u64;
        } segment;
    };
}
