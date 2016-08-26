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

    template<typename VALUE_T>
    class Document_t {
    private:
        uint8_t *body;
        uint32_t nnodes, szstrings;
        uint8_t *types;
        VALUE_T *values;
        char *strings;
        void _setup(void);
        void _recur_count0(const rapidjson::Value *cur);
        void _recur_fill0(const rapidjson::Value *cur, uint32_t curpos,
                          uint32_t *curused, uint32_t *curoffset);
        void _recur_count1(const Document_t<VALUE_T> *doc, uint32_t pos);
        void _recur_fill1(const Document_t<VALUE_T> *doc, uint32_t docpos,
                          uint32_t curpos, uint32_t *curused, uint32_t *curoffset);
        void _sort_object(uint32_t start, int64_t iidx, int64_t jidx);
        rapidjson::Value *_recur_unfreeze(uint32_t pos) const;
    public:
        Document_t(const rapidjson::Value *root);
        Document_t(const Document_t<VALUE_T> *doc, uint32_t docpos);
        inline Document_t(uint8_t *body, uint32_t body_size)
        {   this->body = body; nnodes = *(uint32_t *)body; _setup();
            szstrings = body + body_size - (uint8_t *)strings; }
        inline ~Document_t() { if (body) free(body); }

        inline uint32_t BodySize(void) const
        {   size_t size = sizeof(uint32_t) + nnodes;
            if (size % 8 > 0) size += 8 - size % 8;
            return size + nnodes * sizeof(VALUE_T) + szstrings; }
        inline const uint8_t *Body(void) const { return body; }

        inline rapidjson::Value *Unfreeze(uint32_t pos) const { return _recur_unfreeze(pos); }

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
        uint32_t SearchObject(uint32_t pos, const char *key) const;

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

    template<typename VALUE_T>
    Document_t<VALUE_T>::Document_t(const rapidjson::Value *root)
    {
        nnodes = szstrings = 0;
        _recur_count0(root);
        uint32_t total_size = sizeof(uint32_t) + nnodes;
        if (total_size % 8 > 0) total_size += 8 - total_size % 8;
        total_size += nnodes * sizeof(VALUE_T) + szstrings;
        body = (uint8_t *)malloc(total_size);
        if (body == NULL) return;
        *(uint32_t *)body = nnodes; _setup();
        uint32_t curused = 1, curoffset = 0;
        _recur_fill0(root, 0, &curused, &curoffset);
    }
    template<typename VALUE_T>
    Document_t<VALUE_T>::Document_t(const Document_t<VALUE_T> *doc, uint32_t pos)
    {
        nnodes = szstrings = 0;
        if (doc->IsRemoved(pos)) { body = NULL; types = NULL; values = NULL; strings = NULL; }
        else {
            _recur_count1(doc, pos);
            uint32_t total_size = sizeof(uint32_t) + nnodes;
            if (total_size % 8 > 0) total_size += 8 - total_size % 8;
            total_size += nnodes * sizeof(VALUE_T) + szstrings;
            body = (uint8_t *)malloc(total_size);
            if (body == NULL) return;
            *(uint32_t *)body = nnodes; _setup();
            uint32_t curused = 1, curoffset = 0;
            _recur_fill1(doc, pos, 0, &curused, &curoffset);
        }
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_setup(void)
    {
        uint8_t *cur = body + sizeof(uint32_t);
        types = cur; cur += nnodes;
        if ((cur - body) % 8 > 0) cur += 8 - (cur - body) % 8;
        values = (VALUE_T *)cur; cur += nnodes * sizeof(VALUE_T);
        strings = (char *)cur;
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_recur_count0(const rapidjson::Value *cur)
    {
        ++nnodes;
        if (cur->IsString()) {
            szstrings += cur->GetStringLength() + 1;
        } else if (cur->IsArray()) {
            rapidjson::Value::ConstValueIterator iter;
            for (iter = cur->Begin(); iter != cur->End(); ++iter)
                _recur_count0(&*iter);
        } else if (cur->IsObject()) {
            nnodes += cur->MemberCount();
            rapidjson::Value::ConstMemberIterator iter;
            for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                szstrings += iter->name.GetStringLength() + 1;
                _recur_count0(&iter->value);
            }
        }
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_recur_fill0(const rapidjson::Value *cur, uint32_t curpos,
                                      uint32_t *curused, uint32_t *curoffset)
    {
        if (cur->IsNull()) {
            types[curpos] = fjnull; values[curpos].uint_v = 0;
        } else if (cur->IsFalse()) {
            types[curpos] = fjfalse; values[curpos].uint_v = 0;
        } else if (cur->IsTrue()) {
            types[curpos] = fjtrue; values[curpos].uint_v = 0;
        } else if (cur->IsInt()) {
            types[curpos] = fjint; values[curpos].int_v = cur->GetInt();
        } else if (cur->IsInt64()) {
            types[curpos] = fjint; values[curpos].int_v = cur->GetInt64();
        } else if (cur->IsUint()) {
            types[curpos] = fjuint; values[curpos].uint_v = cur->GetUint();
        } else if (cur->IsUint64()) {
            types[curpos] = fjuint; values[curpos].uint_v = cur->GetUint64();
        } else if (cur->IsDouble()) {
            types[curpos] = fjdouble; values[curpos].double_v = cur->GetDouble();
        } else if (cur->IsString()) {
            uint32_t len = cur->GetStringLength();
            types[curpos] = fjstring;
            values[curpos].string.offset = *curoffset;
            values[curpos].string.len = len;
            strcpy(strings + *curoffset, cur->GetString());
            *curoffset += len + 1;
        } else if (cur->IsArray()) {
            types[curpos] = fjarray;
            uint32_t subpos = values[curpos].array.start = *curused;
            *curused += values[curpos].array.space = cur->Size();
            rapidjson::Value::ConstValueIterator iter;
            for (iter = cur->Begin(); iter != cur->End(); ++iter)
                _recur_fill0(&*iter, subpos++, curused, curoffset);
        } else if (cur->IsObject()) {
            types[curpos] = fjobject;
            uint32_t subpos = values[curpos].object.start = *curused;
            values[curpos].object.space = cur->MemberCount();
            *curused += values[curpos].object.space + values[curpos].object.space;
            rapidjson::Value::ConstMemberIterator iter;
            for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                uint32_t len = iter->name.GetStringLength();
                types[subpos] = fjstring;
                values[subpos].string.offset = *curoffset;
                values[subpos++].string.len = len;
                strcpy(strings + *curoffset, iter->name.GetString());
                *curoffset += len + 1;
                _recur_fill0(&iter->value, subpos++, curused, curoffset);
            }
            if (values[curpos].object.space > 1)
                _sort_object(values[curpos].object.start, 0,
                             (int64_t)(values[curpos].object.space - 1));
        }
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_recur_count1(const Document_t<VALUE_T> *doc, uint32_t docpos)
    {
        ++nnodes;
        if (doc->IsString(docpos)) {
            szstrings += doc->GetStringLen(docpos) + 1;
        } else if (doc->IsArray(docpos)) {
            uint32_t space = doc->GetArraySpace(docpos);
            for (uint32_t idx = 0; idx < space; ++idx) {
                uint32_t subpos = doc->GetArray(docpos, idx);
                if (doc->IsRemoved(subpos)) continue;
                _recur_count1(doc, subpos);
            }
        } else if (doc->IsObject(docpos)) {
            uint32_t space = doc->GetObjectSpace(docpos);
            for (uint32_t idx = 0; idx < space; ++idx) {
                uint32_t subpos = doc->GetObject(docpos, idx);
                if (doc->IsRemoved(subpos)) continue;
                ++nnodes;
                szstrings += doc->GetObjectKeyLen(docpos, idx) + 1;
                _recur_count1(doc, doc->GetObject(docpos, idx));
            }
        }
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_recur_fill1(const Document_t<VALUE_T> *doc, uint32_t docpos,
                                      uint32_t curpos, uint32_t *curused, uint32_t *curoffset)
    {
        if (doc->IsNull(docpos)) {
            types[curpos] = fjnull; values[curpos].uint_v = 0;
        } else if (doc->IsFalse(docpos)) {
            types[curpos] = fjfalse; values[curpos].uint_v = 0;
        } else if (doc->IsTrue(docpos)) {
            types[curpos] = fjtrue; values[curpos].uint_v = 0;
        } else if (doc->IsInt(docpos)) {
            types[curpos] = fjint; values[curpos].int_v = doc->GetInt(docpos);
        } else if (doc->IsUint(docpos)) {
            types[curpos] = fjuint; values[curpos].uint_v = doc->GetUint(docpos);
        } else if (doc->IsDouble(docpos)) {
            types[curpos] = fjdouble; values[curpos].double_v = doc->GetDouble(docpos);
        } else if (doc->IsString(docpos)) {
            types[curpos] = fjstring;
            values[curpos].string.offset = *curoffset;
            values[curpos].string.len = doc->GetStringLen(docpos);
            strcpy(strings + *curoffset, doc->GetString(docpos));
            *curoffset += doc->GetStringLen(docpos) + 1;
        } else if (doc->IsArray(docpos)) {
            types[curpos] = fjarray;
            uint32_t subpos = values[curpos].array.start = *curused;
            uint32_t space = doc->GetArraySpace(docpos);
            uint32_t size = doc->GetArraySize(docpos);
            *curused += values[curpos].array.space = size;
            for (uint32_t idx = 0; idx < space; ++idx) {
                uint32_t docsubpos = doc->GetArray(docpos, idx);
                if (doc->IsRemoved(docsubpos)) continue;
                _recur_fill1(doc, doc->GetArray(docpos, idx), subpos++, curused, curoffset);
            }
        } else if (doc->IsObject(docpos)) {
            types[curpos] = fjobject;
            uint32_t subpos = values[curpos].object.start = *curused;
            uint32_t space = doc->GetObjectSpace(docpos);
            uint32_t size = doc->GetObjectSize(docpos);
            values[curpos].object.space = size;
            *curused += size + size;
            for (uint32_t idx = 0; idx < space; ++idx) {
                uint32_t docsubpos = doc->GetObject(docpos, idx);
                if (doc->IsRemoved(docsubpos)) continue;
                types[subpos] = fjstring;
                values[subpos].string.offset = *curoffset;
                values[subpos++].string.len = doc->GetObjectKeyLen(docpos, idx);
                strcpy(strings + *curoffset, doc->GetObjectKey(docpos, idx));
                *curoffset += doc->GetObjectKeyLen(docpos, idx) + 1;
                _recur_fill1(doc, docsubpos, subpos++, curused, curoffset);
            }
        }
    }
    template<typename VALUE_T>void
    Document_t<VALUE_T>::_sort_object(uint32_t start, int64_t iidx, int64_t jidx)
    {
        int64_t midx, nidx, kidx;
        uint8_t temp0; VALUE_T temp1;
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
        if (midx < jidx) _sort_object(start, midx, jidx);
        if (iidx < nidx) _sort_object(start, iidx, nidx);
    }
    template<typename VLAUE_T>rapidjson::Value *
    Document_t<VALUE_T>::_recur_unfreeze(uint32_t pos) const
    {
        switch (GetType(pos)) {
        case fjnull: return new rapidjson::Value(rapidjson::kNullType);
        case fjfalse: return new rapidjson::Value(rapidjson::kFalseType);
        case fjtrue: return new rapidjson::Value(rapidjson::kTrueType);
        case fjint:// return new rapidjson::Value(rapidjson::kIntType);
        case fjuint: // FIXME.;
        case fjstring: // FIXME.;
        case fjarray: {
            rapidjson::Value *rvalue = new rapidjson::Value(rapidjson::kArrayType);
            for (uint32_t idx = 0; idx < GetArraySize(pos); ++idx) {
                uint32_t subpos = GetArray(pos, idx);
                if (IsRemoved(subpos)) continue;
                rvalue->PushBack(_recur_unfreeze(subpos));
            }
            return rvalule; }
        case fjobject: {
            rapidjson::Value *rvalue = new rapidjson::Value(rapidjson::kObjectType);
            for (uint32_t idx = 0; idx < GetObjectSpace(pos); ++idx) {
                uint32_t subpos = GetObject(pos, idx);
                if (IsRemoved(subpos)) continue;
                rvalue->AddMember(GetObjectKey(pos, idx), _recur_unfreeze(subpos), allocator);
            }
            return rvalue; }
        }
        return NULL;
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
    Document_t<VALUE_T>::SearchObject(uint32_t pos, const char *key) const
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
        char *cur, *next, *_path = strdupa(path);
        for (cur = _path; cur != NULL; cur = next) {
            if ((next = strchr(cur, '.')) != NULL) *next++ = 0;
            if (strlen(cur) == strspn(cur, "0123456789")) {
                if (!IsArray(pos)) return UINT32_MAX;
                uint32_t idx = atol(cur);
                if (idx >= GetArraySpace(pos)) return UINT32_MAX;
                pos = GetArray(pos, idx);
            } else {
                if (!IsObject(pos)) return UINT32_MAX;
                if ((pos = SearchObject(pos, cur)) == UINT32_MAX) return UINT32_MAX;
            }
        }
        return pos;
    }

    typedef Document_t<value4_t> Document4_t;
    typedef Document_t<value8_t> Document8_t;
}
