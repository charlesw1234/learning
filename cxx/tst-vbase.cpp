#include <stdint.h>
#include <stdio.h>

#define SHOWCALL                                                \
    { printf("%s(%u): %p\n", __FUNCTION__, __LINE__, this); }
class base0_t {
public:
    base0_t(void) SHOWCALL;
    virtual ~base0_t() SHOWCALL;
    uint64_t vbase0;
};

class base1_t: virtual public base0_t {
public:
    base1_t(void) SHOWCALL;
    virtual ~base1_t() SHOWCALL;
    uint64_t vbase1;
};

class mid0_t: public base1_t {
public:
    mid0_t(void) SHOWCALL;
    virtual ~mid0_t() SHOWCALL;
    uint64_t vmid0;
};
class mid1_t: public base1_t {
public:
    mid1_t(void) SHOWCALL;
    virtual ~mid1_t() SHOWCALL;
    uint64_t vmid1;
};

class subclass_t: public mid0_t, public mid1_t {
public:
    subclass_t(void) SHOWCALL;
    virtual ~subclass_t() SHOWCALL;
    uint64_t vsubclass;
};

int
main(void)
{
    subclass_t *scobj = new subclass_t();
    base0_t *b0obj = scobj;
    printf("b0obj = %p\n", b0obj);
    printf("dynamic_cast<base1_t *>: %p\n", dynamic_cast<base1_t *>(b0obj));
    printf("dynamic_cast<mid0_t *>: %p\n", dynamic_cast<mid0_t *>(b0obj));
    printf("dynamic_cast<mid1_t *>: %p\n", dynamic_cast<mid1_t *>(b0obj));
    printf("dynamic_cast<subclass_t *>: %p\n", dynamic_cast<subclass_t *>(b0obj));
    delete scobj;
    return 0;
}
