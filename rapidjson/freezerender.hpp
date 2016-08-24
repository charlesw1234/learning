#pragma once

#include "freeze.hpp"
#include "rapidjson/internal/itoa.h"
#include "rapidjson/internal/dtoa.h"

namespace fjson {
    template<class DOC_T>
    class Render_t {
    private:
        char *start, *cur, *last;
        bool _extend(size_t size);
        inline void _put_char(char ch)
        {   if (cur < last || _extend(1)) *cur++ = ch; }
        inline void _put_string(const char *str, size_t slen)
        {   if (cur + slen <= last || _extend(slen)) { memcpy(cur, str, slen); cur += slen; } }

        void _render_int(int64_t value);
        void _render_uint(uint64_t value);
        void _render_double(double value);
        void _render_string(const char *value);
        void _render(const DOC_T *doc, uint32_t pos);
    public:
        inline Render_t(const DOC_T *doc, uint32_t pos)
        {   start = cur = (char *)malloc(4096);
            last = start == NULL ? NULL: start + 4096;
            _render(doc, pos);
            _put_char(0); }
        inline ~Render_t() { if (start) free(start); }

        inline char *get(void) { char *start = this->start; this->start = NULL; return start; }
    };

    template<class DOC_T>bool Render_t<DOC_T>::_extend(size_t nbytes)
    {
        size_t size = last - start;
        while ((cur - start) + nbytes > size) size += size;
        char *newstart = (char *)realloc(start, size);
        if (newstart == NULL) return false;
        cur = newstart + (cur - start);
        last = newstart + size;
        start = newstart;
        return true;
    }
    template<class DOC_T>void Render_t<DOC_T>::_render_int(int64_t value)
    {   char buf[128]; _put_string(buf, rapidjson::internal::i64toa(value, buf) - buf); }
    template<class DOC_T>void Render_t<DOC_T>::_render_uint(uint64_t value)
    {   char buf[128]; _put_string(buf, rapidjson::internal::u64toa(value, buf) - buf); }
    template<class DOC_T>void Render_t<DOC_T>::_render_double(double value)
    {   char buf[128]; _put_string(buf, rapidjson::internal::dtoa(value, buf) - buf); }
    template<class DOC_T>void Render_t<DOC_T>::_render_string(const char *value)
    {
        _put_char('"');
        while (*value) {
            size_t step = strcspn(value, "\"\\\b\f\r\n\t");
            _put_string(value, step);
            value += step;
            switch (*value) {
            case '"': _put_string("\\\"", 2); break;
            case '\\': _put_string("\\\\", 2); break;
            case '\b': _put_string("\\b", 2); break;
            case '\f': _put_string("\\f", 2); break;
            case '\r': _put_string("\\r", 2); break;
            case '\n': _put_string("\\n", 2); break;
            case '\t': _put_string("\\t", 2); break;
            }
        }
        _put_char('"');
    }
    template<class DOC_T>void Render_t<DOC_T>::_render(const DOC_T *doc, uint32_t pos)
    {
        switch (doc->GetType(pos)) {
        case fjremoved: break;
        case fjnull: _put_string("null", 4); break;
        case fjfalse: _put_string("false", 5); break;
        case fjtrue: _put_string("true", 4); break;
        case fjint: _render_int(doc->GetInt(pos)); break;
        case fjuint: _render_uint(doc->GetUint(pos)); break;
        case fjdouble: _render_double(doc->GetDouble(pos)); break;
        case fjstring: _render_string(doc->GetString(pos)); break;
        case fjarray: {
            uint32_t idx, subpos;
            _put_char('[');
            for (idx = 0; idx < doc->GetArraySpace(pos); ++idx) {
                if (idx > 0) _put_char(',');
                subpos = doc->GetArray(pos, idx);
                if (doc->IsRemoved(subpos)) continue;
                _render(doc, subpos);
            }
            _put_char(']');
            break;
        }
        case fjobject: {
            uint32_t idx, subpos;
            _put_char('{');
            for (idx = 0; idx < doc->GetObjectSize(pos); ++idx) {
                if (idx > 0) _put_char(',');
                subpos = doc->GetObject(pos, idx);
                if (doc->IsRemoved(subpos)) continue;
                _render_string(doc->GetObjectKey(pos, idx));
                _put_char(':');
                _render(doc, subpos);
            }
            _put_char('}');
        }
            break;
        }
    }

    typedef Render_t<Document4_t> Render4_t;
    typedef Render_t<Document8_t> Render8_t;
}
