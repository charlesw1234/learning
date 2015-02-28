#ifdef TST_LIST
#include <list>
class intlist: public std::list<unsigned> {};
#endif

#ifdef TST_SET
#include <set>
class intset: public std::set<unsigned> {};
#endif

#ifdef TST_VECTOR
#include <vector>
class intvector: public std::vector<unsigned> {};
#endif

int main(void)
{
    unsigned idx;
#ifdef TST_LIST
    intlist il;
#endif
#ifdef TST_SET
    intset is;
#endif
#ifdef TST_VECTOR
    intvector iv;
#endif

    for (idx = 0; idx < 15; ++idx) {
#ifdef TST_LIST
        il.push_back(idx);
#endif
#ifdef TST_SET
        is.insert(idx);
#endif
#ifdef TST_VECTOR
        iv.resize(idx + 1);
        iv[idx] = idx;
#endif
    }
    return 0;
}
