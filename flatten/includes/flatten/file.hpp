#pragma once

#include "flatten/defs.hpp"

namespace flatten {
    class file_t {
    public:
	inline file_t(const char *fname) { _fp = fopen(fname, "rb+"); }
	inline ~file_t() { if (_fp) fclose(_fp); }

	inline bool read(void *space, size_t position, size_t spacesize)
	{   return fseek(_fp, position, SEEK_SET) == 0 &&
		fread(space, 1, spacesize, _fp) == spacesize; }
	inline bool write(const void *space, size_t position, size_t spacesize)
	{   return fseek(_fp, position, SEEK_SET) == 0 &&
		fwrite(space, 1, spacesize, _fp) == spacesize; }
    private:
        FILE *_fp;
    };
    class memfile_t {
    public:
        inline bool read(void *space, size_t position, size_t spacesize)
        {   return false; }
        inline bool write(const void *space, size_t position, size_t spacesize)
        {   return false; }
    };
}
