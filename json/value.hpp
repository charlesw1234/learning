#pragma once

#include <stdint.h>
#include <stdlib.h>
#include <string.h>

namespace json {
    enum valuetype_t { vtnil, vtbool, vtint, vtunsigned, vtdouble,
                       vtstring, vtarray, vtobject };
    class array_t {
    };
    class object_t {
    };
    class value_t {
    public:
        inline value_t(void) { _type = vtnil; }
        inline value_t(bool vbool) { _type = vtbool; _value._bool = vbool; }
        inline value_t(int vint) { _type = vtint; _value._int = vint; }
        inline value_t(unsigned vunsigned)
        {   _type = vtunsigned; _value._unsigned = vunsigned; }
        inline value_t(double vdouble)
        {   _type = vtdouble; _value._double = vdouble; }
        inline value_t(const char *vstr)
        {   _type = vtstring; _value._string = strdup(vstr); }
        inline value_t(const char *vstr, size_t vstrlen)
        {   _type = vtstring, _value._string = strndup(vstr, vstrlen); }
        value_t(valuetype_t vtype);
        ~value_t();

        inline bool operator ==(const value_t &other) const
        {   return _type == other._type ? _equal(other): false; }
        inline bool operator !=(const value_t &other) const
        {   return _type != other._type ? !_equal(other): false; }
    private:
        uint8_t _type;
        union {
            bool _bool;
            int _int;
            unsigned _unsigned;
            double _double;
            char *_string;
            array_t *_array;
            object_t *_object;
        }  _value;
        bool _equal(const value_t &other) const;
    };
}
