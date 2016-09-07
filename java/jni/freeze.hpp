#pragma once

#include <stdint.h>
#include <stdlib.h>
#include "rapidjson/document.h"

namespace fjson {
    enum type_t { fjremoved, fjnull, fjfalse, fjtrue, fjint, fjuint, fjdouble,
                  fjstring, fjarray, fjobject };
    union value8_t {
        inline const uint32_t magic(void) const { return 0x464A0008; }
        int64_t int_v;
        uint64_t uint_v;
        double double_v;
        struct { uint32_t offset, len; } string;
        struct { uint32_t start, space; } array;
        struct { uint32_t start, space; } object;
    };
    union value4_t {
        inline const uint32_t magic(void) const { return 0x464A0004; }
        int32_t int_v;
        uint32_t uint_v;
        float double_v;
        struct { uint16_t offset, len; } string;
        struct { uint16_t start, space; } array;
        struct { uint16_t start, space; } object;
    };

    struct header_t {
        uint32_t magic;
        uint32_t nnodes;

        inline void setup(uint32_t magic, uint32_t nnodes)
        {   this->magic = magic; this->nnodes = nnodes; }
    };

    template<typename VALUE_T>class Document_t {
        friend class DocumentAuto_t;
    private:
        header_t *body;
        uint32_t nnodes, szstrings;
        uint8_t *types;
        VALUE_T *values;
        char *strings;
        bool _new(uint32_t nnodes, uint32_t szstrings);
        void _setup(void);
        inline Document_t(void) {};
    public:
        Document_t(const rapidjson::Value *root);
        Document_t(const Document_t<VALUE_T> *doc, uint32_t docpos);
#ifdef WITH_PYTHON
        Document_t(PyObject_t *doc);
#endif
        inline Document_t(uint8_t *body, uint32_t body_size)
        {   this->body = (header_t *)body; nnodes = this->body->nnodes; _setup();
            szstrings = ((uint8_t *)body) + body_size - (uint8_t *)strings; }
        inline ~Document_t() { if (body) free(body); }

        inline uint32_t BodySize(void) const
        {   size_t size = sizeof(header_t) + nnodes;
            if (size % sizeof(VALUE_T) > 0) size += sizeof(VALUE_T) - size % sizeof(VALUE_T);
            return size + nnodes * sizeof(VALUE_T) + szstrings; }
        inline const uint8_t *Body(void) const { return (uint8_t *)body; }
        inline uint32_t ValueSize(void) const { return sizeof(VALUE_T); }

        rapidjson::Document *RapidJsonUnfreeze(uint32_t pos) const;
#ifdef WITH_PYTHON
        PyObject_t *PythonUnfreeze(uint32_t pos) const;
#endif

        inline bool IsRemoved(uint32_t pos) const { return types[pos] == fjremoved; }
        inline bool IsNull(uint32_t pos) const { return types[pos] == fjnull; }
        inline bool IsFalse(uint32_t pos) const { return types[pos] == fjfalse; }
        inline bool IsTrue(uint32_t pos) const { return types[pos] == fjtrue; }
        inline bool IsInt(uint32_t pos) const { return types[pos] == fjint; }
        inline bool IsUint(uint32_t pos) const { return types[pos] == fjuint; }
        inline bool IsDouble(uint32_t pos) const { return types[pos] == fjdouble; }
        inline bool IsString(uint32_t pos) const { return types[pos] == fjstring; }
        inline bool IsArray(uint32_t pos) const { return types[pos] == fjarray; }
        inline bool IsObject(uint32_t pos) const { return types[pos] == fjobject; }

        inline type_t GetType(uint32_t pos) const { return (type_t)types[pos]; }
        inline int64_t GetInt(uint32_t pos) const { return values[pos].int_v; }
        inline uint64_t GetUint(uint32_t pos) const { return values[pos].uint_v; }
        inline double GetDouble(uint32_t pos) const { return values[pos].double_v; }
        inline const char *GetString(uint32_t pos) const
        {   return strings + values[pos].string.offset; }
        inline uint32_t GetStringLen(uint32_t pos) const { return values[pos].string.len; }

        inline uint32_t GetArraySpace(uint32_t pos) const { return values[pos].array.space; }
        inline uint32_t GetArraySize(uint32_t pos) const;
        inline uint32_t GetArray(uint32_t pos, uint32_t idx) const
        {   return values[pos].array.start + idx; }

        inline uint32_t GetObjectSpace(uint32_t pos) const { return values[pos].object.space; }
        inline uint32_t GetObjectSize(uint32_t pos) const;
        inline const char *GetObjectKey(uint32_t pos, uint32_t idx) const
        {   return strings + values[values[pos].object.start + idx + idx].string.offset; }
        inline uint32_t GetObjectKeyLen(uint32_t pos, uint32_t idx) const
        {   return values[values[pos].object.start + idx + idx].string.len; }
        inline uint32_t GetObject(uint32_t pos, uint32_t idx) const
        {   return values[pos].object.start + idx + idx + 1; }
        uint32_t ObjectSearch(uint32_t pos, const char *key) const;

        uint32_t Locate(uint32_t pos, const char *path) const;

        inline void SetType(uint32_t pos, type_t type) { types[pos] = (uint8_t)type; }
        inline void Remove(uint32_t pos) { SetType(pos, fjremoved); }
        inline void SetNull(uint32_t pos) { SetType(pos, fjnull); }
        inline void SetFalse(uint32_t pos) { SetType(pos, fjfalse); }
        inline void SetTrue(uint32_t pos) { SetType(pos, fjtrue); }
        inline void SetInt(uint32_t pos, int64_t value)
        {   types[pos] = fjint; values[pos].int_v = value; }
        inline void SetUint(uint32_t pos, uint64_t value)
        {   types[pos] = fjuint; values[pos].uint_v = value; }
        inline void SetDouble(uint32_t pos, double value)
        {   types[pos] = fjdouble; values[pos].double_v = value; }
    };

    template<typename VALUE_T>bool
    Document_t<VALUE_T>::_new(uint32_t nnodes, uint32_t szstrings)
    {
        this->nnodes = nnodes; this->szstrings = szstrings;
        uint32_t total_size = sizeof(header_t) + nnodes;
        if (total_size % sizeof(VALUE_T) > 0)
            total_size += sizeof(VALUE_T) - total_size % sizeof(VALUE_T);
        total_size += nnodes * sizeof(VALUE_T) + szstrings;
        body = (header_t *)malloc(total_size);
        if (body == NULL) return false;
        body->setup(VALUE_T().magic(), nnodes); _setup();
        return true;
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_setup(void)
    {
        uint8_t *start = (uint8_t *)body;
        uint8_t *cur = start + sizeof(header_t);
        types = cur; cur += nnodes;
        unsigned remains = (cur - start) % sizeof(VALUE_T);
        if (remains > 0) {
            memset(cur, 0, sizeof(VALUE_T) - remains);
            cur += sizeof(VALUE_T) - remains;
        }
        values = (VALUE_T *)cur; cur += nnodes * sizeof(VALUE_T);
        strings = (char *)cur;
    }
    template<typename VALUE_T>uint32_t
    Document_t<VALUE_T>::GetArraySize(uint32_t pos) const
    {
        uint32_t size = 0;
        for (uint32_t idx = 0; idx < GetArraySpace(pos); ++idx)
            if (!IsRemoved(GetArray(pos, idx))) ++size;
        return size;
    }
    template<typename VALUE_T>uint32_t
    Document_t<VALUE_T>::GetObjectSize(uint32_t pos) const
    {
        uint32_t size = 0;
        for (uint32_t idx = 0; idx < GetObjectSpace(pos); ++idx)
            if (!IsRemoved(GetObject(pos, idx))) ++size;
        return size;
    }
    template<typename VALUE_T>uint32_t
    Document_t<VALUE_T>::ObjectSearch(uint32_t pos, const char *key) const
    {
        int rc; const char *key1;
        uint32_t idx0 = 0, idx1 = 0, idx2 = values[pos].object.space;
        while (idx0 < idx2) {
            idx1 = (idx0 + idx2) / 2;
            key1 = strings + values[values[pos].object.start + idx1 + idx1].string.offset;
            rc = strcmp(key, key1);
            if (rc < 0) idx2 = idx1;
            else if (rc > 0) idx0 = idx1 + 1;
            else return values[pos].object.start + idx1 + idx1 + 1;
        }
        return UINT32_MAX;
    }

    template<typename VALUE_T>uint32_t
    Document_t<VALUE_T>::Locate(uint32_t pos, const char *path) const
    {
        char *cur, *next, *_path = strdup(path);
        for (cur = _path; cur != NULL; cur = next) {
            if ((next = strchr(cur, '.')) != NULL) *next++ = 0;
            if (strlen(cur) == strspn(cur, "0123456789")) {
                if (!IsArray(pos)) {
                    pos = UINT32_MAX; goto quit0;
                }
                uint32_t idx = atol(cur);
                if (idx >= GetArraySpace(pos)) {
                    pos = UINT32_MAX; goto quit0;
                }
                pos = GetArray(pos, idx);
            } else {
                if (!IsObject(pos)) {
                    pos = UINT32_MAX; goto quit0;
                }
                if ((pos = ObjectSearch(pos, cur)) == UINT32_MAX) {
                    pos = UINT32_MAX; goto quit0;
                }
            }
        }
    quit0:
        free(_path);
        return pos;
    }

    template<typename VALUE_T>class Sort_t {
        uint8_t *types, temp0;
        VALUE_T *values, temp1;
        const char *strings;
    public:
        Sort_t(uint8_t *types, VALUE_T *values, const char *strings):
            types(types), values(values), strings(strings) {}
        void recur_sort(uint32_t start, int64_t iidx, int64_t jidx)
        {
            int64_t midx, nidx, kidx;
            const char *mkey, *nkey, *kkey;
            midx = iidx; nidx = jidx; kidx = (iidx + jidx) / 2;
            kkey = strings + values[start + kidx + kidx].string.offset;
            do {
                while (midx < jidx) {
                    mkey = strings + values[start + midx + midx].string.offset;
                    if (strcmp(mkey, kkey) >= 0) break;
                    ++midx;
                }
                while (nidx > iidx) {
                    nkey = strings + values[start + nidx + nidx].string.offset;
                    if (strcmp(nkey, kkey) <= 0) break;
                    --nidx;
                }
                if (midx <= nidx) {
                    if (midx < nidx) {
                        // swap key.
                        temp0 = types[start + midx + midx];
                        types[start + midx + midx] = types[start + nidx + nidx];
                        types[start + nidx + nidx] = temp0;
                        temp1 = values[start + midx + midx];
                        values[start + midx + midx] = values[start + nidx + nidx];
                        values[start + nidx + nidx] = temp1;
                        // swap value.
                        temp0 = types[start + midx + midx + 1];
                        types[start + midx + midx + 1] = types[start + nidx + nidx + 1];
                        types[start + nidx + nidx + 1] = temp0;
                        temp1 = values[start + midx + midx + 1];
                        values[start + midx + midx + 1] = values[start + nidx + nidx + 1];
                        values[start + nidx + nidx + 1] = temp1;
                    }
                    ++midx; --nidx;
                }
            } while (midx <= nidx);
            if (midx < jidx) recur_sort(start, midx, jidx);
            if (iidx < nidx) recur_sort(start, iidx, nidx);
        }
    };
}

#include "freeze.rapidjson.hpp"
#include "freeze.freeze.hpp"
#ifdef WITH_PYTHON
#include "freeze.python.hpp"
#endif

namespace fjson {
    template<typename VALUE_T>
    Document_t<VALUE_T>::Document_t(const rapidjson::Value *root)
    {
        RapidJsonCount_t countobj;
        countobj.recur_count(root);
        if (!_new(countobj.nnodes, countobj.szstrings)) return;
        RapidJsonFill_t<VALUE_T> fillobj(types, values, strings);
        fillobj.recur_fill(root, 0);
    }
    template<typename VALUE_T>rapidjson::Document *
    Document_t<VALUE_T>::RapidJsonUnfreeze(uint32_t pos) const
    {
        RapidJsonUnfreeze_t<VALUE_T> unfreezeobj(this);
        unfreezeobj.recur_unfreeze(*unfreezeobj.document, pos);
        return unfreezeobj.document;
    }

    template<typename VALUE_T>
    Document_t<VALUE_T>::Document_t(const Document_t<VALUE_T> *doc, uint32_t pos)
    {
        if (doc->IsRemoved(pos)) { body = NULL; types = NULL; values = NULL; strings = NULL; }
        else {
            FreezeCount_t<VALUE_T> countobj;
            countobj.recur_count(doc, pos);
            if (!_new(countobj.nnodes, countobj.szstrings)) return;
            FreezeFill_t<VALUE_T> fillobj(types, values, strings);
            fillobj.recur_fill(doc, pos, 0);
        }
    }

#ifdef WITH_PYTHON
    template<typename VALUE_T>
    Document_t<VALUE_T>::Document_t(PyObject_t *doc)
    {
        PythonCount_t countobj;
        countobj.recur_count(doc);
        if (!_new(countobj.nnodes, countobj.szstrings)) return;
        PythonFill_t<VALUE_T> fillobj(types, values, strings);
        fillobj.recur_fill(doc, 0);
    }
    template<typename VALUE_T>PyObject_t *
    Document_t<VALUE_T>::PythonUnfreeze(uint32_t pos) const
    {
        PythonUnfreeze_t<VALUE_T> unfreezeobj(this);
        return unfreezeobj.recur_unfreeze(pos);
    }
#endif

    typedef Document_t<value4_t> Document4_t;
    typedef Document_t<value8_t> Document8_t;

    static const size_t MaxDocumentSpace =
        sizeof(Document4_t) > sizeof(Document8_t) ? sizeof(Document4_t): sizeof(Document8_t);

#define FJSON_FILL_DOC4(TYPE)                                           \
    TYPE<value4_t> fillobj(this->doc4->types, this->doc4->values, this->doc4->strings)
#define FJSON_FILL_DOC8(TYPE)                                           \
    TYPE<value8_t> fillobj(this->doc8->types, this->doc8->values, this->doc8->strings)

    class DocumentAuto_t {
    private:
        Document4_t *doc4;
        Document8_t *doc8;
        uint8_t space[MaxDocumentSpace];
        bool _new(uint32_t nnodes, uint32_t szstrings, uint64_t imax, int64_t imin)
        {   if ((nnodes & UINT16_MAX) == nnodes && (szstrings & UINT16_MAX) == szstrings &&
                (imax & UINT32_MAX) == imax && (imin & UINT32_MAX) == imin) {
                doc8 = NULL;
                if (!(doc4 = new(space)Document4_t())) return false;
                return doc4->_new(nnodes, szstrings);
            } else {
                doc4 = NULL;
                if (!(doc8 = new(space)Document8_t())) return false;
                return doc8->_new(nnodes, szstrings);
            }
            return false; }
    public:
        inline DocumentAuto_t(const rapidjson::Value *root)
        {   RapidJsonCount_t cobj;
            cobj.recur_count(root);
            if (!_new(cobj.nnodes, cobj.szstrings, cobj.imax, cobj.imin)) return;
            if (this->doc4) {
                FJSON_FILL_DOC4(RapidJsonFill_t); fillobj.recur_fill(root, 0);
            } else if (this->doc8) {
                FJSON_FILL_DOC8(RapidJsonFill_t); fillobj.recur_fill(root, 0); } }
        inline DocumentAuto_t(const Document4_t *doc4, uint32_t docpos)
        {   FreezeCount_t<value4_t> cobj;
            cobj.recur_count(doc4, docpos);
            if (!_new(cobj.nnodes, cobj.szstrings, cobj.imax, cobj.imin)) return;
            if (this->doc4) {
                FJSON_FILL_DOC4(FreezeFill_t); fillobj.recur_fill(this->doc4, docpos, 0); } }
        inline DocumentAuto_t(const Document8_t *doc8, uint32_t docpos)
        {   FreezeCount_t<value8_t> cobj;
            cobj.recur_count(doc8, docpos);
            if (!_new(cobj.nnodes, cobj.szstrings, cobj.imax, cobj.imin)) return;
            if (this->doc4) {
                FJSON_FILL_DOC4(FreezeFill_t); fillobj.recur_fill(this->doc4, docpos, 0);
            } else if(this->doc8) {
                FJSON_FILL_DOC8(FreezeFill_t); fillobj.recur_fill(this->doc8, docpos, 0); } }
        inline DocumentAuto_t(const DocumentAuto_t *doc, uint32_t docpos)
        {   if (doc4) DocumentAuto_t(doc4, docpos);
            else if (doc8) DocumentAuto_t(doc8, docpos); }
#ifdef WITH_PYTHON
        inline DocumentAuto_t(PyObject_t *doc)
        {   PythonCount_t cobj;
            cobj.recur_count(doc);
            if (!_new(cobj.nnodes, cobj.szstrings, cobj.imax, cobj.imin)) return;
            if (this->doc4) {
                FJSON_FILL_DOC4(PythonFill_t); fillobj.recur_fill(doc, 0);
            } else if (this->doc8) {
                FJSON_FILL_DOC8(PythonFill_t); fillobj.recur_fill(doc, 0); } }
#endif
        inline DocumentAuto_t(uint8_t *body, uint32_t body_size)
        {   if (((header_t *)body)->magic == value4_t().magic()) {
                doc8 = NULL; doc4 = new(space)Document4_t(body, body_size);
            } else if (((header_t *)body)->magic == value8_t().magic()) {
                doc4 = NULL; doc8 = new(space)Document8_t(body, body_size);
            } else { doc4 = NULL; doc8 = NULL; } }
        inline ~DocumentAuto_t()
        {   if (doc4) doc4->~Document4_t();
            else if (doc8) doc8->~Document8_t(); }

        inline const Document4_t *getdoc4c(void) const { return doc4; }
        inline Document4_t *getdoc4(void) { return doc4; }
        inline const Document8_t *getdoc8c(void) const { return doc8; }
        inline Document8_t *getdoc8(void) { return doc8; }

        inline uint32_t BodySize(void) const
        {   if (doc4) return doc4->BodySize();
            else if (doc8) return doc8->BodySize();
            else return 0; }
        inline const uint8_t *Body(void) const
        {   if (doc4) return doc4->Body();
            else if (doc8) return doc8->Body();
            return NULL; }
        inline uint32_t ValueSize(void) const
        {   if (doc4) return doc4->ValueSize();
            else if (doc8) return doc8->ValueSize();
            else return 0; }

        inline rapidjson::Document *RapidJsonUnfreeze(uint32_t pos) const
        {   if (doc4) return doc4->RapidJsonUnfreeze(pos);
            else if (doc8) return doc8->RapidJsonUnfreeze(pos);
            return NULL; }
#ifdef WITH_PYTHON
        inline PyObject_t *PythonUnfreeze(uint32_t pos) const
        {   if (doc4) return doc4->PythonUnfreeze(pos);
            else if (doc8) return doc8->PythonUnfreeze(pos);
            return NULL; }
#endif

#define FJSON_AUTO_IS(FUNC) inline bool FUNC(uint32_t pos) const \
        {   if (doc4) return doc4->FUNC(pos);                    \
            else if (doc8) return doc8->FUNC(pos);               \
            else return false; }
        FJSON_AUTO_IS(IsRemoved);
        FJSON_AUTO_IS(IsNull);
        FJSON_AUTO_IS(IsFalse);
        FJSON_AUTO_IS(IsTrue);
        FJSON_AUTO_IS(IsInt);
        FJSON_AUTO_IS(IsUint);
        FJSON_AUTO_IS(IsDouble);
        FJSON_AUTO_IS(IsString);
        FJSON_AUTO_IS(IsArray);
        FJSON_AUTO_IS(IsObject);

#define FJSON_AUTO_GET(TYPE, FUNC, VALUE) inline TYPE FUNC(uint32_t pos) \
        {   if (doc4) return doc4->FUNC(pos);                           \
            else if (doc8) return doc8->FUNC(pos);                      \
            else return VALUE; }
#define FJSON_AUTO_GET2(TYPE, FUNC, VALUE) inline TYPE FUNC(uint32_t pos, uint32_t idx) \
        {   if (doc4) return doc4->FUNC(pos, idx);                      \
            else if (doc8) return doc8->FUNC(pos, idx);                 \
            else return VALUE; }
        FJSON_AUTO_GET(type_t, GetType, fjremoved);
        FJSON_AUTO_GET(int64_t, GetInt, 0);
        FJSON_AUTO_GET(uint64_t, GetUint, 0);
        FJSON_AUTO_GET(double, GetDouble, 0);
        FJSON_AUTO_GET(const char *, GetString, NULL);
        FJSON_AUTO_GET(uint32_t, GetStringLen, 0);

        FJSON_AUTO_GET(uint32_t, GetArraySpace, 0);
        FJSON_AUTO_GET(uint32_t, GetArraySize, 0);
        FJSON_AUTO_GET2(uint32_t, GetArray, 0);

        FJSON_AUTO_GET(uint32_t, GetObjectSpace, 0);
        FJSON_AUTO_GET(uint32_t, GetObjectSize, 0);
        FJSON_AUTO_GET2(const char *, GetObjectKey, NULL);
        FJSON_AUTO_GET2(uint32_t, GetObjectKeyLen, 0);
        FJSON_AUTO_GET2(uint32_t, GetObject, 0);
        inline uint32_t ObjectSearch(uint32_t pos, const char *key) const
        {   if (doc4) return doc4->ObjectSearch(pos, key);
            else if (doc8) return doc8->ObjectSearch(pos, key);
            else return 0; }

        inline uint32_t Locate(uint32_t pos, const char *path) const
        {   if (doc4) return doc4->Locate(pos, path);
            else if (doc8) return doc8->Locate(pos, path);
            else return 0; }

#define FJSON_AUTO_SET(FUNC) inline void FUNC(uint32_t pos) \
        {   if (doc4) doc4->FUNC(pos);                      \
            else if (doc8) doc8->FUNC(pos); }
#define FJSON_AUTO_SET2(FUNC, TYPE) inline void FUNC(uint32_t pos, TYPE value) \
        {   if (doc4) doc4->FUNC(pos, value);                           \
            else if (doc8) doc8->FUNC(pos, value); }
        FJSON_AUTO_SET2(SetType, type_t);
        FJSON_AUTO_SET(Remove);
        FJSON_AUTO_SET(SetNull);
        FJSON_AUTO_SET(SetFalse);
        FJSON_AUTO_SET(SetTrue);
        FJSON_AUTO_SET2(SetInt, int64_t);
        FJSON_AUTO_SET2(SetUint, uint64_t);
        FJSON_AUTO_SET2(SetDouble, double);
    };
}
