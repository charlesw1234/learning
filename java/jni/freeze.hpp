#pragma once

#include <stdint.h>
#include <stdlib.h>
#include "rapidjson/document.h"

namespace fjson {
    union value8_t {
        int64_t int_v;
        uint64_t uint_v;
        double double_v;
        struct { uint32_t offset, len; } string;
        struct { uint32_t start, size; } array;
        struct { uint32_t start, size; } object;
    };
    union value4_t {
        int32_t int_v;
        uint32_t uint_v;
        float double_v;
        struct { uint16_t offset, len; } string;
        struct { uint16_t start, size; } array;
        struct { uint16_t start, size; } object;
    };

    template<typename VALUE_T>
    class Document_t {
    public:
        enum type_t { fjnull, fjfalse, fjtrue, fjint, fjuint, fjdouble,
                      fjstring, fjarray, fjobject };
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

        inline uint32_t GetArraySize(uint32_t pos) const { return values[pos].array.size; }
        inline uint32_t GetArray(uint32_t pos, uint32_t idx) const
        {   return values[pos].array.start + idx; }

        inline uint32_t GetObjectSize(uint32_t pos) const { return values[pos].object.size; }
        inline const char *GetObjectKey(uint32_t pos, uint32_t idx) const
        {   return strings + values[values[pos].object.start + idx + idx].string.offset; }
        inline uint32_t GetObjectKeyLen(uint32_t pos, uint32_t idx) const
        {   return values[values[pos].object.start + idx + idx].string.len; }
        inline uint32_t GetObject(uint32_t pos, uint32_t idx) const
        {   return values[pos].object.start + idx + idx + 1; }
        uint32_t SearchObject(uint32_t pos, const char *key) const;

        uint32_t Locate(uint32_t pos, const char *path) const;
    };
}
