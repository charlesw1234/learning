#include <assert.h>
#include "scanner.hpp"

namespace scanner {
    Scanner_t::Scanner_t(const char *fpath)
    {
        status = st_title;
        title0 = title1 = body0 = body1 = used = buffer;
        gzfile = gzopen(fpath, "rb");
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
            case st_title: goto title;
            case st_body_reported: goto body_reported;
            case st_body: goto body;
            }
        title:
            term = title0 + strcspn(title0, ",\n");
            termch = *term; *term = 0;
            title1 = term;
            body0 = body1 = term + 1;
            if (termch == ',') {
                if (strstr(title0, keyword) == NULL) goto body;
                status = st_body_reported;
                return title0;
            } else if (termch == '\n') {
                backup = title0;
                title0 = title1 = term + 1;
                if (strstr(backup, keyword) == NULL) goto title;
                return backup;
            } else { // termch == 0.
                if (!readmore(0)) break;
                goto title;
            }
        body_reported:
            term = body0 + strcspn(body0, "\n");
            termch = *term; *term = 0;
            body1 = term;
            if (termch == '\n') {
                title0 = title1 = body0 = body1 = term + 1;
                goto title;
            } else { // *term == 0.
                if (!readmore(0)) break;
                goto body_reported;
            }
        body:
            term = body0 + strcspn(body0, "\n");
            termch = *term; *term = 0;
            body1 = term;
            if (strstr(body0, keyword) == NULL) {
                if (!readmore(kept)) break;
                goto body;
            } else if (termch == '\n') {
                backup = title0;
                title0 = title1 = body0 = body1 = term + 1;
                status = st_title;
                return backup;
            } else { // termch == 0.
                backup = title0;
                title0 = title1 = body0 = body1 = term + 1;
                status = st_body_reported;
                return backup;
            }
        }
        return NULL;
    }
    void
    Scanner_t::makespace(size_t kept)
    {
        if (buffer < title0 && title0 < title1) {
            memmove(buffer, title0, title1 - title0);
            title1 = buffer + (title1 - title0);
            title0 = buffer;
        }
        if (body0 + kept < body1) body0 = body1 - kept;
        if (title1 < body0 && body0 < body1) {
            memmove(title1, body0, body1 - body0);
            body1 = title1 + (body1 - body0);
            body0 = title1;
        }
        used = body1;
        used[0] = used[1] = 0;
    }
}
