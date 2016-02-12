#include <assert.h>
#include "value.hpp"

namespace json {
    value_t::value_t(valuetype_t vtype)
    {
        switch (_type = vtype) {
        case vtarray: _value._array = new array_t(); break;
        case vtobject: _value._object = new object_t(); break;
        default: assert(0); }
    }
    value_t::~value_t()
    {
        switch (_type) {
        case vtnil: case vtbool: case vtint: case vtunsigned: case vtdouble: break;
        case vtstring: free(_value._string); break;
        case vtarray: delete(_value._array); break;
        case vtobject: delete(_value._object); break;
        }
    }
    bool value_t::_equal(const value_t &other) const
    {
        switch (_type) {
        case vtnil:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtbool:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtint:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtunsigned:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtdouble:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtstring:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtarray:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        case vtobject:
            switch (other._type) {
            case vtnil:
            case vtbool:
            case vtint:
            case vtunsigned:
            case vtdouble:
            case vtstring:
            case vtarray:
            case vtobject:
            default: assert(0);
            }
        }
    }
}
