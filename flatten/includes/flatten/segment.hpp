#pragma once

#include "flatten/file.hpp"

namespace flatten {
    template<typename SIZE_T>class segment_t {
    public:
        static inline size_t sizeof_size(void) { return sizeof(SIZE_T); }

	inline segment_t(void): _base(0), _size(0) {}
	inline ~segment_t() {}

	inline SIZE_T base(void) const { return _base; }
	inline SIZE_T size(void) const { return _size; }

	inline void setbase(SIZE_T _base) { this->_base = _base; }
	inline void setsize(SIZE_T _size) { this->_size = _size; }

	inline bool load(file_t *file, uint8_t *space) const
	{   return file->read(space, _base, _size); }
        inline bool load(memfile_t *file, uint8_t *space) const
        {   return file->read(space, _base, _size); }

	inline bool save(file_t *file, const uint8_t *space) const
	{   return file->write(space, _base, _size); }
        inline bool save(memfile_t *file, const uint8_t *space) const
        {   return file->write(space, _base, _size); }
    private:
	SIZE_T _base, _size;
    };
}
