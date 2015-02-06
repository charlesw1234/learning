#include <stdio.h>
#include <string>
#include <vector>

class Element_t: public std::string {
public:
    Element_t(const char *name): std::string(name)
    { fprintf(stderr, "Element_t.constructor(%p): %s\n", this, this->c_str()); }
    ~Element_t()
    { fprintf(stderr, "Element_t.destructor(%p): %s\n", this, this->c_str()); }
};

class EV_t: public std::vector<Element_t *> {
public:
    EV_t(void)
    { fprintf(stderr, "EV.constructor(%p): size = %u\n", this, (unsigned)size()); }
    ~EV_t() {
        fprintf(stderr, "EV.destructor(%p): size = %u\n", this, (unsigned)size());
        for (iterator iter = begin(); iter != end(); ++iter)
            delete *iter;
    }
    void dump(const char *prefix, FILE *wfp = stderr) const
    {
        unsigned pos;
        for (const_iterator iter = begin(); iter != end(); ++iter)
            fprintf(stderr, "%sEV(%p) #%02u: [%s]\n", prefix, this,
                    pos = iter - begin(), (*iter)->c_str());
    }
};

static inline void
shiter(EV_t &ev, EV_t::iterator &iter)
{
    unsigned pos;
    fprintf(stderr, "iter = %u, [%s]\n",
            pos = iter - ev.begin(), (*iter)->c_str());
}

int
main(int argc, char *argv[])
{
    unsigned idx, limit = 8;
    EV_t ev;
    EV_t::iterator eviter;
    char nbuf[32];

    for (idx = 0; idx < limit; ++idx) {
        snprintf(nbuf, sizeof(nbuf), "ele#%02u", idx);
        ev.push_back(new Element_t(nbuf));
    }
    ev.dump("(A)");

    eviter = ev.begin(); ++eviter; ++eviter;
    shiter(ev, eviter);
    eviter = ev.insert(eviter, new Element_t("INSERTED A")) + 1;
    shiter(ev, eviter);
    eviter = ev.insert(eviter, new Element_t("INSERTED B")) + 1;
    shiter(ev, eviter);
    eviter = ev.insert(eviter, new Element_t("INSERTED C")) + 1;
    ev.dump("(B)");
    return 0;
}
