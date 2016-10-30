#pragma once

#include "flatten/file.hpp"

namespace flatten {
    template<typename SIZE_T>
    class segment_t {
    public:
	inline segment_t(void): _base(0), _size(0) {}
	inline ~segment_t() {}

	inline bool operator == (const segment_t<SIZE_T> &other) const
	{   return _base == other._base; }
	inline bool operator != (const segment_t<SIZE_T> &other) const
	{   return _base != other._base; }
	inline bool operator < （const segment_t<SIZE_T> &other) const
	{   return _base < other._base; }
	inline bool operator > (const segment<SIZE_T> &other) const
	{   return _base > other._base; }


	inline SIZE_T base(void) const { return _base; }
	inline SIZE_T size(void) const { return _size; }

	inline void setbase(SIZE_T _base) { this->_base = _base; }
	inline void setsize(SIZE_T _size) { this->_size = _size; }

	inline void load(file_t *file, uint8_t *space) const
	{   return file->read(space, _base, _size); }
	inline void save(file_t *file, const uint8_t *space) const
	{   return file->write(space, _base, _size); }
    private:
	SIZE_T _base, _size;
    };

    // how to combine segment_t with space_t?
    class space_t {
    public:
	inline space_t(void): _space(NULL), _free(NULL) {}
	inline ~space_t() { if (_free) free(_free); }
    private:
	uint8_t *_space, *_free;
    };

    template<typename SIZE_T>
    class storage_t: public std::vector<segment_t<SIZE_T> *> {
    public:
	inline storage_t(void): std::vector<segment_t<SIZE_T> *>() {}
	inline ~storage_t()
	{   for (size_t idx = 0; idx < size(); ++idx) delete at(idx); }

	inline void rebase(SIZE_T curbase = 0)
	{   for (size_t idx = 0; idx < size(); ++idx) {
		at(idx)->setbase(curbase); curbase += at(idx)->size(); } }
	inline void resave(file_t *file)
	{   for (size_t idx = 0; idx < size(); ++idx) at(idx)->save(file); }
    };
}
