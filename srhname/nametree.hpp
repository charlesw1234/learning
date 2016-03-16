#pragma once

#include <stdint.h>

namespace nametree {
    typedef uint16_t unichar_t;
    class Tree_t {
    public:
        Tree_t(const uint8_t *body);
        inline ~Tree_t() {}
        uint32_t start, ntails;
        const uint32_t *starts;
        const unichar_t *chars;
        const uint16_t *sizes;
        const unichar_t *tails;
    };
    class Iterator_t {
    public:
        static const uint32_t MAXCHARS = 256;
        Iterator_t(const Tree_t *tree);
        uint32_t get(unichar_t *buf) const;
        bool next(void);
    private:
        const Tree_t *_tree;
        unsigned _top;
        unsigned _stack[MAXCHARS];
        unichar_t _prefix[MAXCHARS];
    };
}
