#include "scanner.hpp"

namespace scanner {
    Scanner_t::Scanner_t(const char *fpath)
    {
        cur = last = buffer;
        gzfile = gzopen(fpath, "rb");
    }
    Scanner_t::~Scanner_t()
    {
        gzclose(gzfile);
    }
    const char *
    Scanner_t::scan(const char *keyword)
    {
        int rc = gzread(gzfile, last, buffer + sizeof(buffer));
        assert(rc >= 0);
        last += rc;
    }
}
