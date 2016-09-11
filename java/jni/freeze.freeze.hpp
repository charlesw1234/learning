#pragma once

namespace fjson {
    template<typename VALUE_T>class FreezeCount_t: public countbase_t {
    public:
        inline FreezeCount_t(void): countbase_t() {}
        void recur_count(const Document_t<VALUE_T> *doc, uint32_t docpos)
        {
            ++nnodes;
            if (doc->IsInt(docpos)) {
                int64_t value = doc->GetInt(docpos);
                if (value < 0) { if (value < imin) imin = value;
                } else { if ((uint64_t)value > imax) imax = (uint64_t)value; }
            } else if (doc->IsUint(docpos)) {
                uint64_t value = doc->GetUint(docpos);
                if (value > imax) imax = value;
            } else if (doc->IsString(docpos)) {
                szstrings += doc->GetStringLen(docpos) + 1;
            } else if (doc->IsArray(docpos)) {
                uint32_t space = doc->GetArraySpace(docpos);
                for (uint32_t idx = 0; idx < space; ++idx) {
                    uint32_t subpos = doc->GetArray(docpos, idx);
                    if (doc->IsRemoved(subpos)) continue;
                    recur_count(doc, subpos);
                }
            } else if (doc->IsObject(docpos)) {
                uint32_t space = doc->GetObjectSpace(docpos);
                for (uint32_t idx = 0; idx < space; ++idx) {
                    uint32_t subpos = doc->GetObject(docpos, idx);
                    if (doc->IsRemoved(subpos)) continue;
                    ++nnodes;
                    szstrings += doc->GetObjectKeyLen(docpos, idx) + 1;
                    recur_count(doc, doc->GetObject(docpos, idx));
                }
            }
        }
    };
    template<typename VALUE_T>class FreezeFill_t {
        uint8_t *types; VALUE_T *values; char *strings;
        uint32_t curused, curoffset;
    public:
        FreezeFill_t(uint8_t *types, VALUE_T *values, char *strings):
            types(types), values(values), strings(strings), curused(1), curoffset(0) {}
        void recur_fill(const Document_t<VALUE_T> *doc, uint32_t docpos, uint32_t curpos)
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
                values[curpos].string.offset = curoffset;
                values[curpos].string.len = doc->GetStringLen(docpos);
                strcpy(strings + curoffset, doc->GetString(docpos));
                curoffset += doc->GetStringLen(docpos) + 1;
            } else if (doc->IsArray(docpos)) {
                types[curpos] = fjarray;
                uint32_t subpos = values[curpos].array.start = curused;
                uint32_t space = doc->GetArraySpace(docpos);
                uint32_t size = doc->GetArraySize(docpos);
                curused += values[curpos].array.space = size;
                for (uint32_t idx = 0; idx < space; ++idx) {
                    uint32_t docsubpos = doc->GetArray(docpos, idx);
                    if (doc->IsRemoved(docsubpos)) continue;
                    recur_fill(doc, doc->GetArray(docpos, idx), subpos++);
                }
            } else if (doc->IsObject(docpos)) {
                types[curpos] = fjobject;
                uint32_t subpos = values[curpos].object.start = curused;
                uint32_t space = doc->GetObjectSpace(docpos);
                uint32_t size = doc->GetObjectSize(docpos);
                values[curpos].object.space = size;
                curused += size + size;
                for (uint32_t idx = 0; idx < space; ++idx) {
                    uint32_t docsubpos = doc->GetObject(docpos, idx);
                    if (doc->IsRemoved(docsubpos)) continue;
                    types[subpos] = fjstring;
                    values[subpos].string.offset = curoffset;
                    values[subpos++].string.len = doc->GetObjectKeyLen(docpos, idx);
                    strcpy(strings + curoffset, doc->GetObjectKey(docpos, idx));
                    curoffset += doc->GetObjectKeyLen(docpos, idx) + 1;
                    recur_fill(doc, docsubpos, subpos++);
                }
            }
        }
    };
}
