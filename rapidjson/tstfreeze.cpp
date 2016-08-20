#include "rapidjson/filereadstream.h"
#include "freeze.cpp"

template<class DOC_T>static bool
recur_cmp_rf(const rapidjson::Value *cur0, const DOC_T *doc, uint32_t cur1)
{
    if (cur0->IsNull()) { return doc->IsNull(cur1);
    } else if (cur0->IsFalse()) { return doc->IsFalse(cur1);
    } else if (cur0->IsTrue()) { return doc->IsTrue(cur1);
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
            if (!recur_cmp_rf(&*iter, doc, doc->GetArray(cur1, idx))) return false;
        return true;
    } else if (cur0->IsObject()) {
        if (!doc->IsObject(cur1)) return false;
        if (cur0->MemberCount() != doc->GetObjectSize(cur1)) return false;
        const char *prevkey = NULL;
        for (uint32_t idx = 0; idx < doc->GetObjectSize(cur1); ++idx) {
            const char *key = doc->GetObjectKey(cur1, idx);
            if (!cur0->HasMember(key)) return false;
            if (prevkey != NULL && strcmp(prevkey, key) >= 0) return false;
            if (!recur_cmp_rf(&cur0->FindMember(key)->value, doc, doc->GetObject(cur1, idx)))
                return false;
            prevkey = key;
        }
        return true;
    }
    return false;
}

template<class DOC_T>static bool
recur_cmp_ff(const DOC_T *doc0, uint32_t cur0, const DOC_T *doc1, uint32_t cur1)
{
    if (doc0->IsNull(cur0)) { return doc1->IsNull(cur1);
    } else if (doc0->IsFalse(cur0)) { return doc1->IsFalse(cur1);
    } else if (doc0->IsTrue(cur0)) { return doc1->IsTrue(cur1);
    } else if (doc0->IsInt(cur0)) {
        return doc1->IsInt(cur1) && doc0->GetInt(cur0) == doc1->GetInt(cur1);
    } else if (doc0->IsUint(cur0)) {
        return doc1->IsUint(cur1) && doc0->GetUint(cur0) == doc1->GetUint(cur1);
    } else if (doc0->IsDouble(cur0)) {
        return doc1->IsDouble(cur1) && doc0->GetDouble(cur0) == doc1->GetDouble(cur1);
    } else if (doc0->IsString(cur0)) {
        return doc1->IsString(cur1) && !strcmp(doc0->GetString(cur0), doc1->GetString(cur1));
    } else if (doc0->IsArray(cur0)) {
        if (!doc1->IsArray(cur1)) return false;
        if (doc0->GetArraySize(cur0) != doc1->GetArraySize(cur1)) return false;
        for (uint32_t idx = 0; idx < doc0->GetArraySize(cur0); ++idx)
            if (!recur_cmp_ff(doc0, doc0->GetArray(cur0, idx),
                              doc1, doc1->GetArray(cur1, idx))) return false;
        return true;
    } else if (doc0->IsObject(cur0)) {
        if (!doc1->IsObject(cur1)) return false;
        if (doc0->GetObjectSize(cur0) != doc1->GetObjectSize(cur1)) return false;
        for (uint32_t idx = 0; idx < doc0->GetObjectSize(cur0); ++idx) {
            if (strcmp(doc0->GetObjectKey(cur0, idx), doc1->GetObjectKey(cur1, idx)))
                return false;
            if (!recur_cmp_ff(doc0, doc0->GetObject(cur0, idx),
                              doc1, doc1->GetObject(cur1, idx))) return false;
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

    fjson::Document8_t fdoc80(&doc);
    fjson::Document4_t fdoc40(&doc);
    printf("cmp_rf8 = %s, cmp_rf4 = %s\n",
           recur_cmp_rf<fjson::Document8_t>(&doc, &fdoc80, 0) ? "true": "false",
           recur_cmp_rf<fjson::Document4_t>(&doc, &fdoc40, 0) ? "true": "false");

    uint32_t pos8 = fdoc80.Locate(0, "syncdata");
    uint32_t pos4 = fdoc40.Locate(0, "syncdata");
    fjson::Document8_t fdoc81(&fdoc80, pos8);
    fjson::Document4_t fdoc41(&fdoc40, pos4);
    printf("cmp_f8f8 = %s, cmp_f4f4 = %s\n",
           recur_cmp_ff<fjson::Document8_t>(&fdoc80, pos8, &fdoc81, 0) ? "true": "false",
           recur_cmp_ff<fjson::Document4_t>(&fdoc40, pos4, &fdoc41, 0) ? "true": "false");
    printf("body8_size = %u, %u\n", (uint32_t)fdoc80.BodySize(), (uint32_t)fdoc81.BodySize());
    printf("body4_size = %u, %u\n", (uint32_t)fdoc40.BodySize(), (uint32_t)fdoc41.BodySize());
    return 0;
}
