#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>

class element_t {
public:
    element_t(unsigned idx) {
        _idx = idx;
        fprintf(stderr, "element_t.constructor: %p, %u\n", this, _idx);
    }
    ~element_t()
    { fprintf(stderr, "element_t.destructor: %p, %u\n", this, _idx); }
private:
    unsigned _idx;
    unsigned _idx0, _idx1, _idx2; // space holder
};

class ev_t: public std::vector<element_t *> {
public:
    ev_t(void) { fprintf(stderr, "ev.constructor: %p\n", this); }
    ~ev_t() { fprintf(stderr, "ev.destructor: %p\n", this); }
};

int
main(int argc, char *argv[])
{
    unsigned idx, limit;
    if (argc < 2) limit = 1;
    else limit = atol(argv[1]);
    fprintf(stderr, "#%u: %lu, %lu\n", __LINE__,
            sizeof(ev_t), sizeof(element_t));
    ev_t ev;
    fprintf(stderr, "#%u\n", __LINE__);
    element_t *ele = new element_t(32);
    for (idx = 0; idx < limit; ++idx) {
        fprintf(stderr, "#%u: idx = %u\n", __LINE__, idx);
        ev.push_back(ele);
    }
    delete ele;
    fprintf(stderr, "#%u: %lu, %lu, %lu\n", __LINE__,
            sizeof(ev_t), sizeof(element_t), sizeof(ev));
    return 0;
}
