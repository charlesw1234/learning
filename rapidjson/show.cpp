#include "show.hpp"

std::string
shvalue(const rapidjson::Value *value)
{
    char buf[64];
    if (value->IsNull()) {
        snprintf(buf, sizeof(buf), "Null@%p", value);
    } else if (value->IsFalse()) {
        snprintf(buf, sizeof(buf), "False@%p", value);
    } else if (value->IsTrue()) {
        snprintf(buf, sizeof(buf), "True@%p", value);
    } else if (value->IsInt()) {
        snprintf(buf, sizeof(buf), "int(%d)@%p", value->GetInt(), value);
    } else if (value->IsUint()) {
        snprintf(buf, sizeof(buf), "uint(%u)@%p", value->GetUint(), value);
    } else if (value->IsInt64()) {
        snprintf(buf, sizeof(buf), "int64(%lld)@%p", (long long)value->GetInt64(), value);
    } else if (value->IsUint64()) {
        snprintf(buf, sizeof(buf), "uint64(%llu)@%p",
                 (unsigned long long)value->GetUint64(), value);
    } else if (value->IsDouble()) {
        snprintf(buf, sizeof(buf), "double(%f)@%p", value->GetDouble(), value);
    } else if (value->IsString()) {
        snprintf(buf, sizeof(buf), "string(%s)@%p", value->GetString(), value);
    } else if (value->IsArray()) {
        snprintf(buf, sizeof(buf), "array(%u)@%p", value->Size(), value);
    } else if (value->IsObject()) {
        snprintf(buf, sizeof(buf), "object(%u)@%p", value->MemberCount(), value);
    } else {
        snprintf(buf, sizeof(buf), "unknown@%p", value);
    }
    return buf;
}

void
sharray(FILE *wfp, unsigned indent, const rapidjson::Value &value)
{
    char fmt[64];
    std::string desc;
    rapidjson::Value::ConstValueIterator iter;
    memset(fmt, ' ', indent);
    snprintf(fmt + indent, sizeof(fmt) - indent, "%s", "[%u]: %s\n");
    for (iter = value.Begin(); iter != value.End(); ++iter) {
        desc = shvalue(&*iter);
        fprintf(wfp, fmt, iter - value.Begin(), desc.c_str());
        if (iter->IsArray()) sharray(wfp, indent + 4, *iter);
        else if (iter->IsObject()) shobject(wfp, indent + 4, *iter);
    }
}
void
shobject(FILE *wfp, unsigned indent, const rapidjson::Value &value)
{
    char fmt[64];
    std::string desc;
    rapidjson::Value::ConstMemberIterator iter;
    memset(fmt, ' ', indent);
    snprintf(fmt + indent, sizeof(fmt) - indent, "%s", "[%s]: %s\n");
    for (iter = value.MemberBegin(); iter != value.MemberEnd(); ++iter) {
        desc = shvalue(&iter->value);
        fprintf(wfp, fmt, iter->name.GetString(), desc.c_str());
        if (iter->value.IsArray()) sharray(wfp, indent + 4, iter->value);
        else if (iter->value.IsObject()) shobject(wfp, indent + 4, iter->value);
    }
}
