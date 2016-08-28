#include "com_wl_www_FreezeDocument4.h"
#include "com_wl_www_FreezeDocument8.h"
#include "com_wl_www_RapidDocument.h"
#include "freeze.hpp"
#include "freezerender.hpp"
#include "rapidjson/writer.h"

#define JNI4FUNC(RET, FUNC) extern "C" JNIEXPORT RET JNICALL    \
    Java_com_wl_www_FreezeDocument4__##FUNC
#define JNI8FUNC(RET, FUNC) extern "C" JNIEXPORT RET JNICALL    \
    Java_com_wl_www_FreezeDocument8__##FUNC
#define JNIRFUNC(RET, FUNC) extern "C" JNIEXPORT RET JNICALL    \
    Java_com_wl_www_RapidDocument__##FUNC

#define JSELF4(JSELF) fjson::Document4_t *self = (fjson::Document4_t *)(JSELF)
#define JSELF8(JSELF) fjson::Document8_t *self = (fjson::Document8_t *)(JSELF)
#define JSELFR(JSELF) rapidjson::Document *self = (rapidjson::Document *)(JSELF)
#define JPOSR(JPOS)   rapidjson::Value *pos = (rapidjson::Value *)(JPOS)

// FreezeDocument?
template<class DOC_T>static inline jlong _Init1(JNIEnv *jenv, jobject jclazz, jstring jdocstr)
{
    rapidjson::Document rdoc;
    const char *docstr = jenv->GetStringUTFChars(jdocstr, 0);
    bool haserror = rdoc.Parse<0>(docstr).HasParseError();
    if (docstr) jenv->ReleaseStringUTFChars(jdocstr, docstr);
    return haserror ? 0: (jlong)new DOC_T(&rdoc);
}
JNI4FUNC(jlong, 1Init__Ljava_lang_String_2)(JNIEnv *jenv, jobject jclazz, jstring jdocstr)
{   return _Init1<fjson::Document4_t>(jenv, jclazz, jdocstr); }
JNI8FUNC(jlong, 1Init__Ljava_lang_String_2)(JNIEnv *jenv, jobject jclazz, jstring jdocstr)
{   return _Init1<fjson::Document8_t>(jenv, jclazz, jdocstr); }

template<class DOC_T>static inline jlong
_Init2(JNIEnv *jenv, jobject jclazz, jobject jother, jlong jpos)
{
    jfieldID fieldid = jenv->GetFieldID(jenv->GetObjectClass(jother), "self", "J");
    DOC_T *other = (DOC_T *)jenv->GetLongField(jother, fieldid);
    return (jlong)new DOC_T(other, (uint32_t)jpos);
}
JNI4FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson4_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jlong jpos)
{   return _Init2<fjson::Document4_t>(jenv, jclazz, jother, jpos); }
JNI8FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson8_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jlong jpos)
{   return _Init2<fjson::Document8_t>(jenv, jclazz, jother, jpos); }

JNI4FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself) { JSELF4(jself); delete self; }
JNI8FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself) { JSELF8(jself); delete self; }

template<class DOC_T>static inline void
_writeObject(JNIEnv *jenv, jobject jclazz, jlong jself, jobject jstream)
{
    jclass jstream_class = jenv->GetObjectClass(jstream);
    jmethodID methodid0 = jenv->GetMethodID(jstream_class, "write", "(I)V");
    jmethodID methodid1 = jenv->GetMethodID(jstream_class, "write", "([BII)V");

    DOC_T *self = (DOC_T *)jself;
    size_t size = self->BodySize();
    jenv->CallVoidMethod(jstream, methodid0, (jint)size);
    jbyteArray jbytearray = jenv->NewByteArray(size);
    jenv->SetByteArrayRegion(jbytearray, 0, size, (const jbyte *)self->Body());
    jenv->CallVoidMethod(jstream, methodid1, jbytearray, 0, size);
    jenv->DeleteLocalRef(jbytearray);
}
JNI4FUNC(void, 1writeObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jobject jstream)
{   return _writeObject<fjson::Document4_t>(jenv, jclazz, jself, jstream); }
JNI8FUNC(void, 1writeObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jobject jstream)
{   return _writeObject<fjson::Document8_t>(jenv, jclazz, jself, jstream); }

template<class DOC_T>static inline jlong
_readObject(JNIEnv *jenv, jobject jclazz, jobject jstream)
{
    jclass jstream_class = jenv->GetObjectClass(jstream);
    jmethodID methodid0 = jenv->GetMethodID(jstream_class, "read", "()I");
    jmethodID methodid1 = jenv->GetMethodID(jstream_class, "read", "([BII)I");
    size_t size = jenv->CallIntMethod(jstream, methodid0);
    uint8_t *body = (uint8_t *)malloc(size);
    if (body == NULL) return (jlong)NULL;
    jbyteArray jbytearray = jenv->NewByteArray(size);
    jenv->CallIntMethod(jstream, methodid1, jbytearray, 0, size);
    memcpy(body, jenv->GetByteArrayElements(jbytearray, 0), size);
    jenv->DeleteLocalRef(jbytearray);
    DOC_T *self = new DOC_T(body, size);
    return (jlong)self;
}
JNI4FUNC(jlong, 1readObject)(JNIEnv *jenv, jobject jclazz, jobject jstream)
{   return _readObject<fjson::Document4_t>(jenv, jclazz, jstream); }
JNI8FUNC(jlong, 1readObject)(JNIEnv *jenv, jobject jclazz, jobject jstream)
{   return _readObject<fjson::Document8_t>(jenv, jclazz, jstream); }

JNI4FUNC(jlong, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELF4(jself); return (jlong)self->BodySize(); }
JNI8FUNC(jlong, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELF8(jself); return (jlong)self->BodySize(); }

JNI4FUNC(jlong, 1Unfreeze)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); rapidjson::Document *doc = new rapidjson::Document();
    self->Unfreeze(*doc, (uint32_t)jpos, doc->GetAllocator());
    return (jlong)doc; }
JNI8FUNC(jlong, 1Unfreeze)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); rapidjson::Document *doc = new rapidjson::Document();
    self->Unfreeze(*doc, (uint32_t)jpos, doc->GetAllocator());
    return (jlong)doc; }

JNI4FUNC(jstring, 1Render)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   fjson::Render4_t render((fjson::Document4_t *)jself, (uint32_t)jpos);
    return jenv->NewStringUTF(render.getc()); }
JNI8FUNC(jstring, 1Render)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   fjson::Render8_t render((fjson::Document8_t *)jself, (uint32_t)jpos);
    return jenv->NewStringUTF(render.getc()); }

JNI4FUNC(jboolean, 1IsRemoved)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsRemoved((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsRemoved)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsRemoved((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsNull((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsNull((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsFalse((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsFalse((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsTrue((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsTrue((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsInt((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsInt((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsUint((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsUint((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsDouble((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsDouble((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsString((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsString((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsArray((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsArray((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jboolean)self->IsObject((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jboolean)self->IsObject((uint32_t)jpos); }

JNI4FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jchar)self->GetType((uint32_t)jpos); }
JNI8FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jchar)self->GetType((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetInt((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetInt((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetUint((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetUint((uint32_t)jpos); }

JNI4FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jdouble)self->GetDouble((uint32_t)jpos); }
JNI8FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jdouble)self->GetDouble((uint32_t)jpos); }

JNI4FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }
JNI8FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }

JNI4FUNC(jlong, 1GetArraySpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetArraySpace((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetArraySpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetArraySpace((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetArraySize((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetArraySize((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF4(jself); return (jlong)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }
JNI8FUNC(jlong, 1GetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF8(jself); return (jlong)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }

JNI4FUNC(jlong, 1GetObjectSpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetObjectSpace((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetObjectSpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetObjectSpace((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); return (jlong)self->GetObjectSize((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); return (jlong)self->GetObjectSize((uint32_t)jpos); }

JNI4FUNC(jstring, 1GetObjectKey)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF4(jself);
    return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }
JNI8FUNC(jstring, 1GetObjectKey)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF8(jself);
    return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }

JNI4FUNC(jlong, 1GetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF4(jself); return (jlong)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }
JNI8FUNC(jlong, 1GetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELF8(jself); return (jlong)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }

template<class DOC_T>static inline jlong
_ObjectSearch(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{
    DOC_T *self = (DOC_T *)jself;
    const char *key = jenv->GetStringUTFChars(jkey, 0);
    uint32_t result = self->ObjectSearch((uint32_t)jpos, key);
    if (key) jenv->ReleaseStringUTFChars(jkey, key);
    return (jlong)result;
}
JNI4FUNC(jlong, 1ObjectSearch)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   return _ObjectSearch<fjson::Document4_t>(jenv, jclazz, jself, jpos, jkey); }
JNI8FUNC(jlong, 1ObjectSearch)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   return _ObjectSearch<fjson::Document8_t>(jenv, jclazz, jself, jpos, jkey); }

template<class DOC_T>static inline jlong
_Locate(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jpath)
{
    DOC_T *self = (DOC_T *)jself;
    const char *path = jenv->GetStringUTFChars(jpath, 0);
    uint32_t result = self->Locate((uint32_t)jpos, path);
    if (path) jenv->ReleaseStringUTFChars(jpath, path);
    return (jlong)result;
}
JNI4FUNC(jlong, 1Locate)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jpath)
{   return _Locate<fjson::Document4_t>(jenv, jclazz, jself, jpos, jpath); }
JNI8FUNC(jlong, 1Locate)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jpath)
{   return _Locate<fjson::Document8_t>(jenv, jclazz, jself, jpos, jpath); }

JNI4FUNC(void, 1Remove)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); self->Remove((uint32_t)jpos); }
JNI8FUNC(void, 1Remove)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); self->Remove((uint32_t)jpos); }

JNI4FUNC(void, 1SetNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); self->SetNull((uint32_t)jpos); }
JNI8FUNC(void, 1SetNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); self->SetNull((uint32_t)jpos); }

JNI4FUNC(void, 1SetFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); self->SetFalse((uint32_t)jpos); }
JNI8FUNC(void, 1SetFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); self->SetFalse((uint32_t)jpos); }

JNI4FUNC(void, 1SetTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF4(jself); self->SetTrue((uint32_t)jpos); }
JNI8FUNC(void, 1SetTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELF8(jself); self->SetTrue((uint32_t)jpos); }

JNI4FUNC(void, 1SetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JSELF4(jself); self->SetInt((uint32_t)jpos, (int64_t)jvalue); }
JNI8FUNC(void, 1SetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JSELF8(jself); self->SetInt((uint32_t)jpos, (int64_t)jvalue); }

JNI4FUNC(void, 1SetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JSELF4(jself); self->SetUint((uint32_t)jpos, (uint64_t)jvalue); }
JNI8FUNC(void, 1SetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JSELF8(jself); self->SetUint((uint32_t)jpos, (uint64_t)jvalue); }

JNI4FUNC(void, 1SetDouble)(JNIEnv *jenv, jobject jclazz,
                           jlong jself, jlong jpos, jdouble jvalue)
{   JSELF4(jself); self->SetDouble((uint32_t)jpos, (double)jvalue); }
JNI8FUNC(void, 1SetDouble)(JNIEnv *jenv, jobject jclazz,
                           jlong jself, jlong jpos, jdouble jvalue)
{   JSELF8(jself); self->SetDouble((uint32_t)jpos, (double)jvalue); }

// RapidDocument.
JNIRFUNC(jlong, 1Init)(JNIEnv *jenv, jobject jclazz, jstring jdocstr)
{   rapidjson::Document *doc = new rapidjson::Document();
    const char *docstr = jenv->GetStringUTFChars(jdocstr, 0);
    bool haserror = doc->Parse<0>(docstr).HasParseError();
    if (docstr) jenv->ReleaseStringUTFChars(jdocstr, docstr);
    return haserror ? 0: (jlong)doc; }
JNIRFUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELFR(jself); delete self; }
JNIRFUNC(jlong, 1GetAllocator)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELFR(jself); return (jlong)&self->GetAllocator(); }

JNIRFUNC(jlong, 1Freeze4)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)new fjson::Document4_t(pos); }
JNIRFUNC(jlong, 1Freeze8)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)new fjson::Document8_t(pos); }

JNIRFUNC(jstring, 1Render)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); rapidjson::StringBuffer buffer;
    rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);
    pos->Accept(writer); return jenv->NewStringUTF(buffer.GetString()); }

JNIRFUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsNull(); }
JNIRFUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsFalse(); }
JNIRFUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsTrue(); }
JNIRFUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsInt(); }
JNIRFUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsUint(); }
JNIRFUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsDouble(); }
JNIRFUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsString(); }
JNIRFUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsArray(); }
JNIRFUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jboolean)pos->IsObject(); }

JNIRFUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)pos->GetInt(); }
JNIRFUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)pos->GetUint(); }
JNIRFUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jdouble)pos->GetDouble(); }
JNIRFUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return jenv->NewStringUTF(pos->GetString()); }

JNIRFUNC(jlong, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)pos->Size(); }
JNIRFUNC(jlong, 1GetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JPOSR(jpos); return (jlong)&(*pos)[jidx]; }

JNIRFUNC(jlong, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); return (jlong)pos->MemberCount(); }
JNIRFUNC(jstring, 1GetObjectKey)(JNIEnv *jenv, jobject jclazz,
                                 jlong jself, jlong jpos, jlong jidx)
{   JPOSR(jpos); rapidjson::Value::MemberIterator iter = pos->MemberBegin() + jidx;
    return jenv->NewStringUTF(iter->name.GetString()); }
JNIRFUNC(jlong, 1GetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JPOSR(jpos); rapidjson::Value::MemberIterator iter = pos->MemberBegin() + jidx;
    return (jlong)&iter->value; }
JNIRFUNC(jlong, 1ObjectSearch)(JNIEnv *jenv, jobject jclazz,
                               jlong jself, jlong jpos, jstring jkey)
{   JPOSR(jpos);
    const char *key = jenv->GetStringUTFChars(jkey, 0);
    jlong subvalue = (jlong)&(*pos)[key];
    if (key) jenv->ReleaseStringUTFChars(jkey, key);
    return subvalue; }

JNIRFUNC(jlong, 1Locate)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jpath)
{   JPOSR(jpos); /* FIXME. */ }

JNIRFUNC(void, 1SetNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->SetNull(); }
JNIRFUNC(void, 1SetFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->SetBool(false); }
JNIRFUNC(void, 1SetTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->SetBool(true); }
JNIRFUNC(void, 1SetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JPOSR(jpos); pos->SetInt((int64_t)jvalue); }
JNIRFUNC(void, 1SetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jvalue)
{   JPOSR(jpos); pos->SetUint((uint64_t)jvalue); }
JNIRFUNC(void, 1SetDouble)(JNIEnv *jenv, jobject jclazz,
                           jlong jself, jlong jpos, jdouble jvalue)
{   JPOSR(jpos); pos->SetDouble((double)jvalue); }
JNIRFUNC(void, 1SetString)(JNIEnv *jenv, jobject jclazz,
                           jlong jself, jlong jpos, jstring jvalue)
{   JSELFR(jself); JPOSR(jpos);
    const char *value = jenv->GetStringUTFChars(jvalue, 0);
    pos->SetString(value, self->GetAllocator());
    if (value) jenv->ReleaseStringUTFChars(jvalue, value); }
JNIRFUNC(void, 1SetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->SetArray(); }
JNIRFUNC(void, 1SetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->SetObject(); }

// Array operations.
JNIRFUNC(void, 1ArrayClean)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->Clear(); }
JNIRFUNC(jlong, 1ArrayAppendNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELFR(jself); JPOSR(jpos); rapidjson::Value value;
    return (jlong)pos->PushBack(value, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayAppend__JJZ)(JNIEnv *jenv, jobject jclazz,
                                   jlong jself, jlong jpos, jboolean jvalue)
{   JSELFR(jself); JPOSR(jpos);
    return (jlong)pos->PushBack((bool)jvalue, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayAppend__JJJ)(JNIEnv *jenv, jobject jclazz,
                                   jlong jself, jlong jpos, jlong jvalue)
{   JSELFR(jself); JPOSR(jpos);
    return (jlong)pos->PushBack((long)jvalue, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayAppend__JJD)(JNIEnv *jenv, jobject jclazz,
                                   jlong jself, jlong jpos, jdouble jvalue)
{   JSELFR(jself); JPOSR(jpos);
    return (jlong)pos->PushBack((double)jvalue, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayAppend__JJLjava_lang_String2)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jvalue)
{   JSELFR(jself); JPOSR(jpos);
    const char *cxxvalue = jenv->GetStringUTFChars(jvalue, 0);
    rapidjson::Value value(cxxvalue, strlen(cxxvalue));
    jlong subvalue = (jlong)pos->PushBack(value, self->GetAllocator()).End();
    if (cxxvalue) jenv->ReleaseStringUTFChars(jvalue, cxxvalue);
    return subvalue; }
JNIRFUNC(jlong, 1ArrayAppendArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELFR(jself); JPOSR(jpos); rapidjson::Value value(rapidjson::kArrayType);
    return (jlong)pos->PushBack(value, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayAppendObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JSELFR(jself); JPOSR(jpos); rapidjson::Value value(rapidjson::kObjectType);
    return (jlong)pos->PushBack(value, self->GetAllocator()).End(); }
JNIRFUNC(jlong, 1ArrayRemove)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jlong jidx)
{   JSELFR(jself); JPOSR(jpos); return (jlong)pos->Erase(pos->Begin() + jidx); }

// Object operations.
#define JKEYR0(JKEY)                                            \
    const char *cxxkey = jenv->GetStringUTFChars((JKEY), 0);    \
    rapidjson::Value key(cxxkey, strlen(cxxkey))
#define JKEYR1(JKEY)                                            \
    if (cxxkey) jenv->ReleaseStringUTFChars((JKEY), cxxkey)

JNIRFUNC(void, 1ObjectClean)(JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos)
{   JPOSR(jpos); pos->RemoveAllMembers(); }
JNIRFUNC(jlong, 1ObjectAddNull)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey); rapidjson::Value value;
    jlong subvalue = (jlong)&pos->AddMember(key, value, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAdd__JJLjava_lang_String2Z)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey, jboolean jvalue)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey);
    jlong subvalue = (jlong)&pos->AddMember(key, (bool)jvalue, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAdd__JJLjava_lang_String2J)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey, jlong jvalue)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey);
    jlong subvalue = (jlong)&pos->AddMember(key, (long)jvalue, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAdd__JJLjava_lang_String2D)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey, jdouble jvalue)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey);
    jlong subvalue = (jlong)&pos->AddMember(key, (double)jvalue, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAdd__JJLjava_lang_String2Ljava_lang_String2)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey, jstring jvalue)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey);
    const char *cxxvalue = jenv->GetStringUTFChars(jvalue, 0);
    rapidjson::Value value(cxxvalue, strlen(cxxvalue));
    jlong subvalue = (jlong)&pos->AddMember(key, value, self->GetAllocator());
    if (cxxvalue) jenv->ReleaseStringUTFChars(jvalue, cxxvalue);
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAddArray)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey); rapidjson::Value value(rapidjson::kArrayType);
    jlong subvalue = (jlong)&pos->AddMember(key, value, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jlong, 1ObjectAddObject)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   JSELFR(jself); JPOSR(jpos); JKEYR0(jkey); rapidjson::Value value(rapidjson::kObjectType);
    jlong subvalue = (jlong)&pos->AddMember(key, value, self->GetAllocator());
    JKEYR1(jkey); return subvalue; }
JNIRFUNC(jboolean, 1ObjectRemove)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jlong jpos, jstring jkey)
{   JSELFR(jself); JPOSR(jpos);
    const char *key = jenv->GetStringUTFChars(jkey, 0);
    jboolean result = pos->RemoveMember(key);
    if (key) jenv->ReleaseStringUTFChars(jkey, key);
    return result; }
