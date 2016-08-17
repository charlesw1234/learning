#include "rapidjson/filereadstream.h"
#include "freeze.hpp"

static bool
recur_cmp(const rapidjson::Value *cur0, const fjson::Document_t *doc, uint32_t cur1)
{
    if (cur0->IsNull()) {
        return doc->IsNull(cur1);
    } else if (cur0->IsFalse()) {
        return doc->IsFalse(cur1);
    } else if (cur0->IsTrue()) {
        return doc->IsTrue(cur1);
    } else if (cur0->IsInt()) {
        return doc->IsInt(cur1) && cur0->GetInt() == doc->GetInt(cur1);
    } else if (cur0->IsInt64()) {
        return doc->IsInt(cur1) && cur0->GetInt64() == doc->GetInt(cur1);
    } else if (cur0->IsUint()) {
        return doc->IsUint(cur1) && cur0->GetUint() == doc->GetUint(cur1);
    } else if (cur0->IsUint64()) {
        return doc->IsUint(cur1) && cur0->GetUint64() == doc->GetUint(cur1);
    } else if (cur0->IsDouble()) {
        return doc->IsDouble(cur1) && cur0->GetDouble() == doc->GetDouble(cur1);
    } else if (cur0->IsString()) {
        return doc->IsString(cur1) && !strcmp(cur0->GetString(), doc->GetString(cur1));
    } else if (cur0->IsArray()) {
        if (!doc->IsArray(cur1)) return false;
        if (cur0->Size() != doc->GetArraySize(cur1)) return false;
        uint32_t idx; rapidjson::Value::ConstValueIterator iter;
        for (idx = 0, iter = cur0->Begin(); idx < doc->GetArraySize(cur1); ++idx, ++iter)
            if (!recur_cmp(&*iter, doc, doc->GetArray(cur1, idx))) return false;
        return true;
    } else if (cur0->IsObject()) {
        if (!doc->IsObject(cur1)) return false;
        if (cur0->MemberCount() != doc->GetObjectSize(cur1)) return false;
        const char *prevkey = NULL;
        for (uint32_t idx = 0; idx < doc->GetObjectSize(cur1); ++idx) {
            const char *key = doc->GetObjectKey(cur1, idx);
            if (!cur0->HasMember(key)) return false;
            if (prevkey != NULL && strcmp(prevkey, key) >= 0) return false;
            if (!recur_cmp(&cur0->FindMember(key)->value, doc, doc->GetObject(cur1, idx)))
                return false;
            prevkey = key;
        }
        return true;
    }
    return false;
}
int main(void)
{
    char buffer[4096];
    rapidjson::Document doc;
    FILE *rfp = fopen("config.json", "r");
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    fclose(rfp);
    fjson::Document_t fdoc(&doc);
    printf("cmp = %s\n", recur_cmp(&doc, &fdoc, 0) ? "true": "false");
    return 0;
}
