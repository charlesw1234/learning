#pragma once

#include <stdint.h>
#include <stdlib.h>
#include "rapidjson/document.h"

namespace fjson {
    enum type_t { fjremoved, fjnull, fjfalse, fjtrue, fjint, fjuint, fjdouble,
                  fjstring, fjarray, fjobject };
    union value8_t {
        int64_t int_v;
        uint64_t uint_v;
        double double_v;
        struct { uint32_t offset, len; } string;
        struct { uint32_t start, space; } array;
        struct { uint32_t start, space; } object;
    };
    union value4_t {
        int32_t int_v;
        uint32_t uint_v;
        float double_v;
        struct { uint16_t offset, len; } string;
        struct { uint16_t start, space; } array;
        struct { uint16_t start, space; } object;
    };

    typedef rapidjson::Document::AllocatorType Allocator;
    template<typename VALUE_T>
    class Document_t {
    private:
        uint8_t *body;
        uint32_t nnodes, szstrings;
        uint8_t *types;
        VALUE_T *values;
        char *strings;
        void _setup(void);
        void _recur_unfreeze(rapidjson::Value &value, uint32_t pos, Allocator &allocator) const;
    public:
        Document_t(const rapidjson::Value *root);
        Document_t(const Document_t<VALUE_T> *doc, uint32_t docpos);
#ifdef WITH_PYTHON
        Document_t(PyObject_t *doc);
#endif
        inline Document_t(uint8_t *body, uint32_t body_size)
        {   this->body = body; nnodes = *(uint32_t *)body; _setup();
            szstrings = body + body_size - (uint8_t *)strings; }
        inline ~Document_t() { if (body) free(body); }

        inline uint32_t BodySize(void) const
        {   size_t size = sizeof(uint32_t) + nnodes;
            if (size % 8 > 0) size += 8 - size % 8;
            return size + nnodes * sizeof(VALUE_T) + szstrings; }
        inline const uint8_t *Body(void) const { return body; }

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

    template<typename VALUE_T>void
    Document_t<VALUE_T>::_setup(void)
    {
        uint8_t *cur = body + sizeof(uint32_t);
        types = cur; cur += nnodes;
        if ((cur - body) % 8 > 0) cur += 8 - (cur - body) % 8;
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
        nnodes = countobj.nnodes; szstrings = countobj.szstrings;
        uint32_t total_size = sizeof(uint32_t) + nnodes;
        if (total_size % 8 > 0) total_size += 8 - total_size % 8;
        total_size += nnodes * sizeof(VALUE_T) + szstrings;
        body = (uint8_t *)malloc(total_size);
        if (body == NULL) return;
        *(uint32_t *)body = nnodes; _setup();
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
            nnodes = countobj.nnodes; szstrings = countobj.szstrings;
            uint32_t total_size = sizeof(uint32_t) + nnodes;
            if (total_size % 8 > 0) total_size += 8 - total_size % 8;
            total_size += nnodes * sizeof(VALUE_T) + szstrings;
            body = (uint8_t *)malloc(total_size);
            if (body == NULL) return;
            *(uint32_t *)body = nnodes; _setup();
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
        nnodes = countobj.nnodes; szstrings = countobj.szstrings;
        uint32_t total_size = sizeof(uint32_t) + nnodes;
        if (total_size % 8 > 0) total_size += 8 - total_size % 8;
        total_size += nnodes * sizeof(VALUE_T) + szstrings;
        body = (uint8_t *)malloc(total_size);
        if (body == NULL) return;
        *(uint32_t *)body = nnodes; _setup();
        PythonFill_t<VALUE_T> fillobj(types, values, strings);
        fillobj.recur_fill(doc, 0);
    }
    template<typename VALUE_T> PyObject_t *
    Document_t<VALUE_T>::PythonUnfreeze(uint32_t pos) const
    {
        PythonUnfreeze_t<VALUE_T> unfreezeobj(this);
        return unfreezeobj.recur_unfreeze(pos);
    }
#endif

    typedef Document_t<value4_t> Document4_t;
    typedef Document_t<value8_t> Document8_t;
}
