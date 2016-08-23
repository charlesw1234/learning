#include "freeze.hpp"

namespace fjson {
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

    typedef Document_t<value8_t> Document8_t;
    typedef Document_t<value4_t> Document4_t;
}
