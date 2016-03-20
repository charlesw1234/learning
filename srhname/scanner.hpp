#pragma once

#include <assert.h>
#include <string.h>
#include <zlib.h>

namespace scanner {
    class Scanner_t {
    public:
        Scanner_t(const char *fpath);
        ~Scanner_t();

        const char *scan(const char *keyword);
    private:
        gzFile gzfile;
        char buffer[16384], *title0, *title1, *body0, *body1, *used;
        enum { st_title, st_body_reported, st_body } status;
        void makespace(size_t kept);
        inline bool readmore(size_t kept)
        {
            makespace(kept);
            int rc = gzread(gzfile, used, buffer + sizeof(buffer) - used - 2);
            assert(rc >= 0);
            used += rc; used[0] = used[1] = 0;
            return rc > 0;
        }
    };
}
