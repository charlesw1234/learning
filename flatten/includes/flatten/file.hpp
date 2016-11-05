#pragma once

#include "flatten/defs.hpp"

namespace flatten {
    class file_t {
    public:
	inline file_t(FILE *fp): _fp(fp) {}
	inline ~file_t() {}

	inline bool read(void *space, size_t position, size_t spacesize)
	{   return fseek(_fp, position, SEEK_SET) == 0 &&
		fread(space, 1, spacesize, _fp) == spacesize; }
	inline bool write(const void *space, size_t position, size_t spacesize)
	{   return fseek(_fp, position, SEEK_SET) == 0 &&
		fwrite(space, 1, spacesize, _fp) == spacesize; }
    private:
        FILE *_fp;
    };
    class memfile_t: public std::vector<uint8_t *> {
    public:
        inline memfile_t(size_t size): _size(size), _bodysize(0) {}
        inline ~memfile_t() { for (size_t idx = 0; idx < size(); ++idx) free(at(idx)); }

        inline bool read(void *space, size_t position, size_t spacesize)
        {   size_t idx, start, bytes;
            if (position + spacesize > _bodysize) return false;
            idx = position / _size; start = position % _size;
            while (spacesize > 0) {
                bytes = std::min(spacesize, _size - start);
                memcpy(space, at(idx) + start, bytes);
                ++idx; start = 0; space = (uint8_t *)space + bytes; spacesize -= bytes;
            }
            return true; }
        inline bool write(const void *space, size_t position, size_t spacesize)
        {   size_t idx, start, bytes;
            if (_bodysize < position + spacesize) {
                _bodysize = position + spacesize;
                while (_bodysize > size() * _size)
                    push_back((uint8_t *)calloc(_size, 1));
            }
            idx = position / _size; start = position % _size;
            while (spacesize > 0) {
                bytes = std::min(spacesize, _size - start);
                memcpy(at(idx) + start, space, bytes);
                ++idx; start = 0; space = (uint8_t *)space + bytes; spacesize -= bytes;
            }
            return true; }

        inline bool dump(FILE *fp)
        {   size_t idx, bytes, cursize, curbodysize = 0;
            for (idx = 0; idx < size(); ++idx) {
                bytes = std::min(_size, _bodysize - curbodysize);
                if ((cursize = fwrite(at(idx), 1, bytes, fp)) < bytes) return false;
                curbodysize += cursize;
            }
            return true; }
    private:
        size_t _size, _bodysize;
    };
}
