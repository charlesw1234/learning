#pragma once

#include <stdint.h>
#include <stdlib.h>
#include "rapidjson/document.h"

namespace fjson {
    class Document_t {
    public:
        enum type_t { fjnull, fjfalse, fjtrue, fjint, fjuint, fjdouble,
                      fjstring, fjarray, fjobject };
    private:
        union value_t {
            int64_t int_v;
            uint64_t uint_v;
            double double_v;
            uint64_t string_offset;
            struct { uint32_t start, size; } array;
            struct { uint32_t start, size; } object;
        };
        uint8_t *body;
        uint32_t nnodes;
        uint8_t *types;
        value_t *values;
        char *strings;
        void _setup(void);
        void _recur_count(const rapidjson::Value *cur, uint32_t *total_strings);
        void _recur_fill(const rapidjson::Value *cur, uint32_t curpos,
                         uint32_t *curused, uint32_t *curoffset);
        void _sort_object(uint32_t start, uint32_t num);
    public:
        Document_t(const rapidjson::Value *root);
        inline Document_t(uint8_t *body)
        {   this->body = body; nnodes = *(uint32_t *)body; _setup(); }
        inline ~Document_t() { if (body) free(body); }

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
        {   return strings + values[pos].string_offset; }

        inline uint32_t GetArraySize(uint32_t pos) const { return values[pos].array.size; }
        inline uint32_t GetArrayAt(uint32_t pos, uint32_t idx) const
        {   return values[pos].array.start + idx; }

        inline uint32_t GetObjectSize(uint32_t pos) const { return values[pos].object.size; }
        inline const char *GetObjectKey(uint32_t pos, uint32_t idx) const
        {   return strings + values[values[pos].object.start + idx + idx].string_offset; }
        inline uint32_t GetObject(uint32_t pos, uint32_t idx) const
        {   return values[pos].object.start + idx + idx + 1; }
        uint32_t SearchObject(uint32_t pos, const char *key) const;
    };
}
