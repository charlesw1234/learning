#include <stdio.h>
#include <typeinfo>
#include <chrono>

class base_t {
public:
    inline base_t(void) {}
    virtual ~base_t() {}
};
class derived_t: public base_t {
public:
    inline derived_t(void): base_t() {}
    virtual ~derived_t() {}
};

int
main(void)
{
    unsigned nidx = 6553600;
    base_t *baseptr = new derived_t();
    std::chrono::system_clock::time_point tpstart, tpend;
    std::chrono::duration<double> duration;

    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        if ((derived_t *)(baseptr) == NULL);
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f\n", "traditional cast", duration.count());

    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        if (static_cast<derived_t *>(baseptr) == NULL);
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f\n", "static_cast", duration.count());

    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        if (dynamic_cast<derived_t *>(baseptr) == NULL);
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f\n", "dynamic_cast", duration.count());

    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        if (typeid(baseptr) == typeid(derived_t *));
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f\n", "typeid(pointer)", duration.count());

    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        if (typeid(*baseptr) == typeid(derived_t));
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f\n", "typeid(instance)", duration.count());

    delete baseptr;
    return 0;
}
