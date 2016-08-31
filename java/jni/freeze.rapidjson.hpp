#pragma once

#include "rapidjson/document.h"

namespace fjson {
    class RapidJsonCount_t {
    public:
        uint32_t nnodes, szstrings;
        RapidJsonCount_t(void): nnodes(0), szstrings(0) {}
        void recur_count(const rapidjson::Value *cur) {
            ++nnodes;
            if (cur->IsString()) {
                szstrings += cur->GetStringLength() + 1;
            } else if (cur->IsArray()) {
                rapidjson::Value::ConstValueIterator iter;
                for (iter = cur->Begin(); iter != cur->End(); ++iter)
                    recur_count(&*iter);
            } else if (cur->IsObject()) {
                nnodes += cur->MemberCount();
                rapidjson::Value::ConstMemberIterator iter;
                for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                    szstrings += iter->name.GetStringLength() + 1;
                    recur_count(&iter->value);
                }
            }
        }
    };
    template<typename VALUE_T>class RapidJsonFill_t {
        uint8_t *types; VALUE_T *values; char *strings;
        uint32_t curused, curoffset;
    public:
        RapidJsonFill_t(uint8_t *types, VALUE_T *values, char *strings):
            types(types), values(values), strings(strings), curused(1), curoffset(0) {}
        void recur_fill(const rapidjson::Value *cur, uint32_t curpos)
        {
            if (cur->IsNull()) { types[curpos] = fjnull;
                values[curpos].uint_v = 0;
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
                values[curpos].string.offset = curoffset;
                values[curpos].string.len = len;
                strcpy(strings + curoffset, cur->GetString());
                curoffset += len + 1;
            } else if (cur->IsArray()) {
                types[curpos] = fjarray;
                uint32_t subpos = values[curpos].array.start = curused;
                curused += values[curpos].array.space = cur->Size();
                rapidjson::Value::ConstValueIterator iter;
                for (iter = cur->Begin(); iter != cur->End(); ++iter)
                    recur_fill(&*iter, subpos++);
            } else if (cur->IsObject()) {
                types[curpos] = fjobject;
                uint32_t subpos = values[curpos].object.start = curused;
                values[curpos].object.space = cur->MemberCount();
                curused += values[curpos].object.space + values[curpos].object.space;
                rapidjson::Value::ConstMemberIterator iter;
                for (iter = cur->MemberBegin(); iter != cur->MemberEnd(); ++iter) {
                    uint32_t len = iter->name.GetStringLength();
                    types[subpos] = fjstring;
                    values[subpos].string.offset = curoffset;
                    values[subpos++].string.len = len;
                    strcpy(strings + curoffset, iter->name.GetString());
                    curoffset += len + 1;
                    recur_fill(&iter->value, subpos++);
                }
                if (values[curpos].object.space > 1) {
                    Sort_t<VALUE_T> sortobj(types, values, strings);
                    sortobj.recur_sort(values[curpos].object.start, 0,
                                       (int64_t)(values[curpos].object.space - 1));
                }
            }
        }
    };
    template<typename VALUE_T>class RapidJsonUnfreeze_t {
        const Document_t<VALUE_T> *doc;
    public:
        rapidjson::Document *document;
        RapidJsonUnfreeze_t(const Document_t<VALUE_T> *doc): doc(doc)
        {   document = new rapidjson::Document(); }
        void recur_unfreeze(rapidjson::Value &value, uint32_t pos)
        {
            switch (doc->GetType(pos)) {
            case fjremoved: break;
            case fjnull: value.SetNull(); break;
            case fjfalse: value.SetBool(false); break;
            case fjtrue: value.SetBool(true); break;
            case fjint: value.SetInt64(doc->GetInt(pos)); break;
            case fjuint: value.SetUint64(doc->GetUint(pos)); break;
            case fjdouble: value.SetDouble(doc->GetDouble(pos)); break;
            case fjstring:
                value.SetString(doc->GetString(pos), document->GetAllocator()); break;
            case fjarray:
                value.SetArray();
                for (uint32_t idx = 0; idx < doc->GetArraySpace(pos); ++idx) {
                    uint32_t subpos = doc->GetArray(pos, idx);
                    if (doc->IsRemoved(subpos)) continue;
                    rapidjson::Value subvalue;
                    recur_unfreeze(subvalue, subpos);
                    value.PushBack(subvalue, document->GetAllocator());
                }
                break;
            case fjobject:
                value.SetObject();
                for (uint32_t idx = 0; idx < doc->GetObjectSpace(pos); ++idx) {
                    uint32_t subpos = doc->GetObject(pos, idx);
                    if (doc->IsRemoved(subpos)) continue;
                    rapidjson::Value subvalue;
                    rapidjson::Value keyvalue(doc->GetObjectKey(pos, idx),
                                              document->GetAllocator());
                    recur_unfreeze(subvalue, subpos);
                    value.AddMember(keyvalue, subvalue, document->GetAllocator());
                }
                break;
            }
        }
    };
}
