#include "com_wl_www_FreezeJson4.h"
#include "com_wl_www_FreezeJson8.h"
#include "freeze.hpp"

#define JNI4FUNC(RET, FUNC) extern "C" JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson4__##FUNC
#define JNI8FUNC(RET, FUNC) extern "C" JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson8__##FUNC
#define JSELF4(JENV, JSELF) fjson::Document4_t *self = (fjson::Document4_t *)(JSELF)
#define JSELF8(JENV, JSELF) fjson::Document8_t *self = (fjson::Document8_t *)(JSELF)

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
_Init2(JNIEnv *jenv, jobject jclazz, jobject jother, jint jpos)
{
    jfieldID fieldid = jenv->GetFieldID(jenv->GetObjectClass(jother), "self", "J");
    DOC_T *other = (DOC_T *)jenv->GetLongField(jother, fieldid);
    return (jlong)new DOC_T(other, (uint32_t)jpos);
}
JNI4FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson4_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jint jpos)
{   return _Init2<fjson::Document4_t>(jenv, jclazz, jother, jpos); }
JNI8FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson8_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jint jpos)
{   return _Init2<fjson::Document8_t>(jenv, jclazz, jother, jpos); }

JNI4FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   delete (fjson::Document4_t *)jself; }
JNI8FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   delete (fjson::Document8_t *)jself; }

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

JNI4FUNC(jint, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELF4(jenv, jself); return (jint)self->BodySize(); }
JNI8FUNC(jint, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
{   JSELF8(jenv, jself); return (jint)self->BodySize(); }

JNI4FUNC(jboolean, 1IsRemoved)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsRemoved((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsRemoved)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsRemoved((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsNull((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsNull((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsFalse((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsFalse((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsTrue((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsTrue((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsInt((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsInt((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsUint((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsUint((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsDouble((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsDouble((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsString((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsString((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsArray((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsArray((uint32_t)jpos); }

JNI4FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jboolean)self->IsObject((uint32_t)jpos); }
JNI8FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jboolean)self->IsObject((uint32_t)jpos); }

JNI4FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jchar)self->GetType((uint32_t)jpos); }
JNI8FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jchar)self->GetType((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jlong)self->GetInt((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jlong)self->GetInt((uint32_t)jpos); }

JNI4FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jlong)self->GetUint((uint32_t)jpos); }
JNI8FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jlong)self->GetUint((uint32_t)jpos); }

JNI4FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jdouble)self->GetDouble((uint32_t)jpos); }
JNI8FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jdouble)self->GetDouble((uint32_t)jpos); }

JNI4FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }
JNI8FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }

JNI4FUNC(jint, 1GetArraySpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jint)self->GetArraySpace((uint32_t)jpos); }
JNI8FUNC(jint, 1GetArraySpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jint)self->GetArraySpace((uint32_t)jpos); }

JNI4FUNC(jint, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jint)self->GetArraySize((uint32_t)jpos); }
JNI8FUNC(jint, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jint)self->GetArraySize((uint32_t)jpos); }

JNI4FUNC(jint, 1GetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF4(jenv, jself); return (jint)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }
JNI8FUNC(jint, 1GetArray)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF8(jenv, jself); return (jint)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }

JNI4FUNC(jint, 1GetObjectSpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jint)self->GetObjectSpace((uint32_t)jpos); }
JNI8FUNC(jint, 1GetObjectSpace)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jint)self->GetObjectSpace((uint32_t)jpos); }

JNI4FUNC(jint, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF4(jenv, jself); return (jint)self->GetObjectSize((uint32_t)jpos); }
JNI8FUNC(jint, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos)
{   JSELF8(jenv, jself); return (jint)self->GetObjectSize((uint32_t)jpos); }

JNI4FUNC(jstring, 1GetObjectKey)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF4(jenv, jself);
    return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }
JNI8FUNC(jstring, 1GetObjectKey)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF8(jenv, jself);
    return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }

JNI4FUNC(jint, 1GetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF4(jenv, jself); return (jint)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }
JNI8FUNC(jint, 1GetObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jint jidx)
{   JSELF8(jenv, jself); return (jint)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }

template<class DOC_T>static inline jint
_SearchObject(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jkey)
{
    DOC_T *self = (DOC_T *)jself;
    const char *key = jenv->GetStringUTFChars(jkey, 0);
    uint32_t result = self->SearchObject((uint32_t)jpos, key);
    if (key) jenv->ReleaseStringUTFChars(jkey, key);
    return (jint)result;
}
JNI4FUNC(jint, 1SearchObject)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jkey)
{   return _SearchObject<fjson::Document4_t>(jenv, jclazz, jself, jpos, jkey); }
JNI8FUNC(jint, 1SearchObject)
    (JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jkey)
{   return _SearchObject<fjson::Document8_t>(jenv, jclazz, jself, jpos, jkey); }

template<class DOC_T>static inline jint
_Locate(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jpath)
{
    DOC_T *self = (DOC_T *)jself;
    const char *path = jenv->GetStringUTFChars(jpath, 0);
    uint32_t result = self->Locate((uint32_t)jpos, path);
    if (path) jenv->ReleaseStringUTFChars(jpath, path);
    return (jint)result;
}
JNI4FUNC(jint, 1Locate)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jpath)
{   return _Locate<fjson::Document4_t>(jenv, jclazz, jself, jpos, jpath); }
JNI8FUNC(jint, 1Locate)(JNIEnv *jenv, jobject jclazz, jlong jself, jint jpos, jstring jpath)
{   return _Locate<fjson::Document8_t>(jenv, jclazz, jself, jpos, jpath); }
