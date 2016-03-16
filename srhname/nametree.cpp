#include "nametree.hpp"

namespace nametree {
    // Tree_t.
    Tree_t::Tree_t(const uint8_t *body)
    {
        uint32_t nnodes = *(const uint32_t *)body; body += sizeof(uint32_t);
        ntails = *(const uint32_t *)body; body += sizeof(uint32_t);
        starts = (const uint32_t *)body; body = (const uint8_t *)(starts + nnodes);
        chars = (const unichar_t *)body; body = (const uint8_t *)(chars + nnodes);
        sizes = (const uint16_t *)body; body = (const uint8_t *)(sizes + nnodes);
        tails = (const unichar_t *)body; body = (const uint8_t *)(tails + ntails);
    }

    // Iterator_t.
    Iterator_t::Iterator_t(const Tree_t *tree)
    {
        unsigned idx = tree->start;
        _tree = tree;
        _top = 0;
        _stack[0] = idx;
        _prefix[0] = _tree->chars[idx];
        ++_top;
        while (tree->sizes[idx] > 0 && tree->sizes[idx] < INT16_MAX) {
            idx = _tree->starts[idx];
            _stack[_top] = idx;
            _prefix[_top] = _tree->chars[idx];
            ++_top;
        }
    }
    uint32_t
    Iterator_t::get(unichar_t *buf) const
    {
        uint32_t idxbuf, idxtail, termtail;
        for (idxbuf = 0; idxbuf < _top - 1; ++idxbuf) buf[idxbuf] = _prefix[idxbuf + 1];
        if (_tree->sizes[_top - 1] > INT16_MAX) {
            idxtail = _tree->starts[_top - 1];
            termtail = idxtail + UINT16_MAX - _tree->sizes[_top - 1];
            while (idxtail < termtail)
                buf[idxbuf++] = _tree->tails[idxtail++];
        }
        buf[idxbuf] = 0;
        return idxbuf;
    }
    bool
    Iterator_t::next(void)
    {
        // pop phase.
        while (true) {
            if (++_stack[_top - 1] > _tree->start) return false;
            if (_stack[_top - 1] < _tree->starts[_top - 2] + _tree->sizes[_top - 2]) break;
            --_top;
        }
        // push phase.
        _prefix[_top - 1] = _tree->chars[_stack[_top - 1]];
        while (_tree->sizes[_stack[_top - 1]] > 0 &&
               _tree->sizes[_stack[_top - 1]] < INT16_MAX) {
            _stack[_top] = _tree->starts[_stack[_top - 1]];
            _prefix[_top] = _tree->chars[_stack[_top - 1]];
            ++_top;
        }
        return true;
    }
}
