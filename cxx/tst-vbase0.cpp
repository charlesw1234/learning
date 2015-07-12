#include <stdio.h>

#define CONSTRUCTOR                                                     \
    {   this->value = value;                                            \
        printf("%s(%u): %p(%u)\n", __FUNCTION__, __LINE__, this, value); }
#define DESTRUCTOR \
    {   printf("%s(%u): %p(%u)\n", __FUNCTION__, __LINE__, this, value); }
class base0_t {
public:
    base0_t(unsigned value) CONSTRUCTOR;
    virtual ~base0_t() DESTRUCTOR;
private:
    unsigned value;
};

class base1_t: public base0_t {
public:
    base1_t(unsigned value): base0_t(value + 10) CONSTRUCTOR;
    virtual ~base1_t() DESTRUCTOR;
private:
    unsigned value;
};

class mid0_t: virtual public base1_t {
public:
    mid0_t(unsigned value): base1_t(value + 100) CONSTRUCTOR;
    virtual ~mid0_t() DESTRUCTOR;
private:
    unsigned value;
};
class mid1_t: virtual public base1_t {
public:
    mid1_t(unsigned value): base1_t(value + 200) CONSTRUCTOR;
    virtual ~mid1_t() DESTRUCTOR;
private:
    unsigned value;
};

class subclass_t: public mid0_t, public mid1_t {
public:
    subclass_t(unsigned value):
        base1_t(value + 3000), mid0_t(value + 1000), mid1_t(value + 2000)
        CONSTRUCTOR;
    virtual ~subclass_t() DESTRUCTOR;
private:
    unsigned value;
};

int
main(void)
{
    subclass_t *scobj = new subclass_t(9);
    base0_t *b0obj = scobj;
    printf("b0obj = %p\n", b0obj);
    printf("dynamic_cast<base1_t *>: %p\n", dynamic_cast<base1_t *>(b0obj));
    printf("dynamic_cast<mid0_t *>: %p\n", dynamic_cast<mid0_t *>(b0obj));
    printf("dynamic_cast<mid1_t *>: %p\n", dynamic_cast<mid1_t *>(b0obj));
    printf("dynamic_cast<subclass_t *>: %p\n", dynamic_cast<subclass_t *>(b0obj));
    delete scobj;
    return 0;
}
