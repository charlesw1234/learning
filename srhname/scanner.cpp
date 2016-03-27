#include <assert.h>
#include "scanner.hpp"

namespace scanner {
    Scanner_t::Scanner_t(const char *fpath)
    {
        status = st_id;
        id0 = id1 = body0 = body1 = used = buffer;
        gzfile = gzopen(fpath, "rb");
        moreid();
    }
    Scanner_t::~Scanner_t()
    {
        gzclose(gzfile);
    }
    const char *
    Scanner_t::scan(const char *keyword)
    {
        size_t kept = strlen(keyword) - 1;
        char *term, *backup, termch;
        for (;;) {
            switch (status) {
            case st_id: goto id;
            case st_body: goto body;
            case st_body_reported: goto body_reported;
            }
        id:
            term = id0 + strcspn(id0, ",");
            termch = *term; *term = 0;
            id1 = term;
            body0 = body1 = term + 1;
            if (termch == 0) {
                if (!moreid()) break;
                goto id;
            }
        body:
            term = body0 + strcspn(body0, "\n");
            termch = *term; *term = 0;
            body1 = term;
            if (strstr(body0, keyword) == NULL) {
                if (termch == '\n') {
                    id0 = id1 = body0 = body1 = term + 1;
                    goto id;
                } else { // termch == 0.
                    if (!morebody(kept)) break;
                    goto body;
                }
            } else {
                if (termch == '\n') {
                    backup = id0;
                    id0 = id1 = body0 = body1 = term + 1;
                    status = st_id;
                    return backup;
                } else { // termch == 0.
                    backup = id0;
                    id0 = id1 = body0 = body1 = term + 1;
                    status = st_body_reported;
                    return backup;
                }
            }
        body_reported:
            term = body0 + strcspn(body0, "\n");
            termch = *term; *term = 0;
            body1 = term;
            if (termch == '\n') {
                id0 = id1 = body0 = body1 = term + 1;
                goto id;
            } else { // *term == 0.
                if (!morebody(0)) break;
                goto body_reported;
            }
        }
        return NULL;
    }
    bool
    Scanner_t::moreid(void)
    {
        if (buffer < id0) {
            if (id0 < id1) memmove(buffer, id0, id1 - id0);
            id1 = buffer + (id1 - id0);
            id0 = buffer;
            used = id1;
        }
        body0 = body1 = id1 + 1;
        return readmore();
    }
    bool
    Scanner_t::morebody(size_t kept)
    {
        if (buffer < id0) {
            assert(*id1 == 0);
            memmove(buffer, id0, id1 + 1 - id0);
            id1 = buffer + (id1 - id0);
            id0 = buffer;
        }
        if (body0 + kept < body1) body0 = body1 - kept;
        if (id1 + 1 < body0) {
            if (body0 < body1) memmove(id1 + 1, body0, body1 - body0);
            body1 = id1 + 1 + (body1 - body0);
            body0 = id1 + 1;
        }
        used = body1;
        return readmore();
    }
}
