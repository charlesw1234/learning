#include "freeze.hpp"

namespace fjson {
    Document_t::Document_t(const rapidjson::Value *root)
    {
        uint32_t total_strings = 0;
        nnodes = 0;
        _recur_count(root, &total_strings);
        uint32_t total_size = sizeof(uint32_t) + nnodes;
        if (total_size % 8 > 0) total_size += 8 - (total_size % 8);
        total_size += nnodes * sizeof(value_t) + total_strings;
        body = (uint8_t *)malloc(total_size);
        if (body == NULL) return;
        *(uint32_t *)body = nnodes; _setup();
        uint32_t curused = 1, curoffset = 0;
        _recur_fill(root, 0, &curused, &curoffset);
    }
    void
    Document_t::_setup(void)
    {
        uint8_t *cur = body + sizeof(uint32_t);    
        types = cur; cur += nnodes;
        if ((cur - body) % 8 > 0) cur += 8 - (cur - body) % 8;
        values = (value_t *)cur; cur += nnodes * sizeof(value_t);
        strings = (char *)cur;
    }
    void
    Document_t::_recur_count(const rapidjson::Value *cur, uint32_t *total_strings)
    {
        ++nnodes;
        if (cur->IsString()) {
            *total_strings += cur->GetStringLength() + 1;
        } else if (cur->IsArray()) {
            rapidjson::Value::ConstValueIterator iter;
            for (iter = cur->Begin(); iter != cur->End(); ++iter)
                _recur_count(&*iter, total_strings);
        } else if (cur->IsObject()) {
            nnodes += cur->MemberCount();
            rapidjson::Value::ConstMemberIterator iter;
            for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                *total_strings += iter->name.GetStringLength() + 1;
                _recur_count(&iter->value, total_strings);
            }
        }
    }
    void
    Document_t::_recur_fill(const rapidjson::Value *cur, uint32_t curpos,
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
            types[curpos] = fjstring; values[curpos].string_offset = *curoffset;
            strcpy(strings + *curoffset, cur->GetString());
            *curoffset += cur->GetStringLength() + 1;
        } else if (cur->IsArray()) {
            types[curpos] = fjarray;
            uint32_t subpos = values[curpos].array.start = *curused;
            *curused += values[curpos].array.size = cur->Size();
            rapidjson::Value::ConstValueIterator iter;
            for (iter = cur->Begin(); iter != cur->End(); ++iter)
                _recur_fill(&*iter, subpos++, curused, curoffset);
        } else if (cur->IsObject()) {
            types[curpos] = fjobject;
            uint32_t subpos = values[curpos].object.start = *curused;
            values[curpos].object.size = cur->MemberCount();
            *curused += values[curpos].object.size + values[curpos].object.size;
            rapidjson::Value::ConstMemberIterator iter;
            for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                types[subpos] = fjstring;
                values[subpos++].string_offset = *curoffset;
                strcpy(strings + *curoffset, iter->name.GetString());
                *curoffset += iter->name.GetStringLength() + 1;
                _recur_fill(&iter->value, subpos++, curused, curoffset);
            }
            if (values[curpos].object.size > 1)
                _sort_object(values[curpos].object.start, 0,
                             (int64_t)(values[curpos].object.size - 1));
        }
    }
    void
    Document_t::_sort_object(uint32_t start, int64_t iidx, int64_t jidx)
    {
        int64_t midx, nidx, kidx;
        uint8_t temp0; value_t temp1;
        const char *mkey, *nkey, *kkey;
        midx = iidx; nidx = jidx; kidx = (iidx + jidx) / 2;
        kkey = strings + values[start + kidx + kidx].string_offset;
        do {
            while (midx < jidx) {
                mkey = strings + values[start + midx + midx].string_offset;
                if (strcmp(mkey, kkey) >= 0) break;
                ++midx;
            }
            while (nidx > iidx) {
                nkey = strings + values[start + nidx + nidx].string_offset;
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

    uint32_t
    Document_t::SearchObject(uint32_t pos, const char *key) const
    {
        int rc; const char *key1;
        uint32_t idx0 = 0, idx1 = 0, idx2 = values[pos].object.size;
        while (idx0 < idx2) {
            idx1 = (idx0 + idx2) / 2;
            key1 = strings + values[values[pos].object.start + idx1 + idx1].string_offset;
            rc = strcmp(key, key1);
            if (rc < 0) idx2 = idx1;
            else if (rc > 0) idx0 = idx1 + 1;
            else return values[pos].object.start + idx1 + idx1 + 1;
        }
        return UINT32_MAX;
    }

    uint32_t
    Document_t::Locate(uint32_t pos, const char *path) const
    {
        char *cur, *next, *_path = strdupa(path);
        for (cur = _path; cur != NULL; cur = next) {
            if ((next = strchr(cur, '.')) != NULL) *next++ = 0;
            if (strlen(cur) == strspn(cur, "0123456789")) {
                if (!IsArray(pos)) return UINT32_MAX;
                uint32_t idx = atol(cur);
                if (idx >= GetArraySize(pos)) return UINT32_MAX;
                pos = GetArray(pos, idx);
            } else {
                if (!IsObject(pos)) return UINT32_MAX;
                if ((pos = SearchObject(pos, cur)) == UINT32_MAX) return UINT32_MAX;
            }
        }
        return pos;
    }
}
