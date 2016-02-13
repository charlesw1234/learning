#include "rapidjson/document.h"
#include "rapidjson/filereadstream.h"

static std::string
shvalue(const rapidjson::Value &value)
{
    char buf[64];
    if (value.IsNull()) {
        snprintf(buf, sizeof(buf), "Null");
    } else if (value.IsFalse()) {
        snprintf(buf, sizeof(buf), "False");
    } else if (value.IsTrue()) {
        snprintf(buf, sizeof(buf), "True");
    } else if (value.IsInt()) {
        snprintf(buf, sizeof(buf), "int(%d)", value.GetInt());
    } else if (value.IsUint()) {
        snprintf(buf, sizeof(buf), "uint(%u)", value.GetUint());
    } else if (value.IsInt64()) {
        snprintf(buf, sizeof(buf), "int64(%lld)", (long long)value.GetInt64());
    } else if (value.IsUint64()) {
        snprintf(buf, sizeof(buf), "uint64(%llu)", (unsigned long long)value.GetUint64());
    } else if (value.IsDouble()) {
        snprintf(buf, sizeof(buf), "double(%f)", value.GetDouble());
    } else if (value.IsString()) {
        snprintf(buf, sizeof(buf), "string(%s)", value.GetString());
    } else if (value.IsArray()) {
        snprintf(buf, sizeof(buf), "array(%u)", value.Size());
    } else if (value.IsObject()) {
        snprintf(buf, sizeof(buf), "object(%u)", value.MemberCount());
    } else {
        snprintf(buf, sizeof(buf), "unknown");
    }
    return buf;
}

static void shobject(unsigned indent, const rapidjson::Value &value);
static void
sharray(unsigned indent, const rapidjson::Value &value)
{
    char fmt[64];
    std::string desc;
    rapidjson::Value::ConstValueIterator iter;
    memset(fmt, ' ', indent);
    snprintf(fmt + indent, sizeof(fmt) - indent, "%s", "[%u]: %s\n");
    for (iter = value.Begin(); iter != value.End(); ++iter) {
        desc = shvalue(*iter);
        printf(fmt, iter - value.Begin(), desc.c_str());
        if (iter->IsArray()) sharray(indent + 4, *iter);
        else if (iter->IsObject()) shobject(indent + 4, *iter);
    }
}
static void
shobject(unsigned indent, const rapidjson::Value &value)
{
    char fmt[64];
    std::string desc;
    rapidjson::Value::ConstMemberIterator iter;
    memset(fmt, ' ', indent);
    snprintf(fmt + indent, sizeof(fmt) - indent, "%s", "[%s]: %s\n");
    for (iter = value.MemberBegin(); iter != value.MemberEnd(); ++iter) {
        desc = shvalue(iter->value);
        printf(fmt, iter->name.GetString(), desc.c_str());
        if (iter->value.IsArray()) sharray(indent + 4, iter->value);
        else if (iter->value.IsObject()) shobject(indent + 4, iter->value);
    }
}

int main(void)
{
    char buffer[4096];
    rapidjson::Document doc;
    FILE *rfp = fopen("config.json", "r");
    rapidjson::FileReadStream fstrm(rfp, buffer, sizeof(buffer));
    doc.ParseStream(fstrm);
    shobject(0, doc);
    fclose(rfp);
    return 0;
}
