#include <stdio.h>
#include <typeinfo>
#include <chrono>

class base_t {
public:
    virtual unsigned get(void) const { return 0; }
};

#define DERIVED(NUM)                                    \
    class derived_##NUM##_t: public base_t {            \
    public:                                             \
    virtual unsigned get(void) const { return NUM; }    \
    }

DERIVED(1);
DERIVED(2);
DERIVED(3);
DERIVED(4);
DERIVED(5);
DERIVED(6);
DERIVED(7);
DERIVED(8);

#define FUNC(NUM)                                       \
    static unsigned func##NUM(void) { return NUM; }
typedef unsigned (*func_t)(void);

FUNC(1);
FUNC(2);
FUNC(3);
FUNC(4);
FUNC(5);
FUNC(6);
FUNC(7);
FUNC(8);

int
main(void)
{
    unsigned total, nidx = 65536000;
    std::chrono::system_clock::time_point tpstart, tpend;
    std::chrono::duration<double> duration;
    derived_1_t d1obj;
    derived_2_t d2obj;
    derived_3_t d3obj;
    derived_4_t d4obj;
    derived_5_t d5obj;
    derived_6_t d6obj;
    derived_7_t d7obj;
    derived_8_t d8obj;
    base_t *objs[8] = { &d1obj, &d2obj, &d3obj, &d4obj, &d5obj, &d6obj, &d7obj, &d8obj };
    func_t funcs[8] = { func1, func2, func3, func4, func5, func6, func7, func8 };

    total = 0;
    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        total += objs[idx % 8]->get();
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f, total = %u\n", "virtual", duration.count(), total);

    total = 0;
    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        total += funcs[idx % 8]();
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f, total = %u\n", "func pointer", duration.count(), total);

    total = 0;
    tpstart = std::chrono::system_clock::now();
    for (unsigned idx = 0; idx < nidx; ++idx)
        switch (idx % 8) {
        case 0: total += 1; break;
        case 1: total += 2; break;
        case 2: total += 3; break;
        case 3: total += 4; break;
        case 4: total += 5; break;
        case 5: total += 6; break;
        case 6: total += 7; break;
        case 7: total += 8; break;
        }
    tpend = std::chrono::system_clock::now();
    duration = tpend - tpstart;
    printf("duration(%20s) = %f, total = %u\n", "switch", duration.count(), total);

    return 0;
}
