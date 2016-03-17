#pragma once

namespace scanner {
    class Scanner_t {
    public:
        Scanner_t(const char *fpath);
        ~Scanner_t();

        const char *scan(const char *keyword);
    private:
        gzFile gzfile;
        char buffer[16384], *cur, *last;
    };
}
