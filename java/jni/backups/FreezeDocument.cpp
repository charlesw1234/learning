#include "com_wl_www_FreezeDocument.h"
#include "freeze.cpp"

extern "C" {
#define JNI_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeDocument__##FUNC

    JNI_FUNC(jlong, 1Init__Ljava_lang_String_2)(JNIEnv *jenv, jobject clazz, jstring jdocstr)
    {   rapidjson::Document rdoc;
        const char *docstr = jenv->GetStringUTFChars(jdocstr, 0);
        bool haserror = rdoc.Parse<0>(docstr).HasParseError();
        if (docstr) jenv->ReleaseStringUTFChars(jdocstr, docstr);
        return haserror ? 0: (jlong)new fjson::Document8_t(&rdoc); }
    JNI_FUNC(jlong, 1Init__Lcom_wl_www_FreezeDocument_2I)
    (JNIEnv *jenv, jobject clazz, jobject jother, jint pos)
    {   jfieldID fieldid = jenv->GetFieldID(jenv->GetObjectClass(jother), "cxxobject", "L");
        fjson::Document8_t *other = (fjson::Document8_t *)jenv->GetLongField(jother, fieldid);
        return (jlong)new fjson::Document8_t(other, (uint32_t)pos); }
    JNI_FUNC(void, 1Free)(JNIEnv *jenv, jobject clazz, jlong self)
    {   delete (fjson::Document8_t *)self; }

    JNI_FUNC(jint, 1BodySize)(JNIEnv *jenv, jobject clazz, jlong self)
    {   return (jint)((fjson::Document8_t *)self)->BodySize(); }
    JNI_FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsFalse((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsTrue((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsInt((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsUint((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsDouble)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsDouble((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsString((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsArray((uint32_t)pos); }
    JNI_FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->IsObject((uint32_t)pos); }

    JNI_FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jchar)((fjson::Document8_t *)self)->GetType((uint32_t)pos); }
    JNI_FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jlong)((fjson::Document8_t *)self)->GetInt((uint32_t)pos); }
    JNI_FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jlong)((fjson::Document8_t *)self)->GetUint((uint32_t)pos); }
    JNI_FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jdouble)((fjson::Document8_t *)self)->GetDouble((uint32_t)pos); }
    JNI_FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject clazz, jlong jself, jint pos)
    {   fjson::Document8_t *self = (fjson::Document8_t *)jself;
        const char *result = self->GetString((uint32_t)pos);
        return jenv->NewStringUTF(result); }
    JNI_FUNC(jint, 1GetArraySize)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->GetArraySize((uint32_t)pos); }
    JNI_FUNC(jint, 1GetArray)(JNIEnv *jenv, jobject clazz, jlong self, jint pos, jint idx)
    {   return (jint)((fjson::Document8_t *)self)->GetArray((uint32_t)pos, (uint32_t)idx); }
    JNI_FUNC(jint, 1GetObjectSize)(JNIEnv *jenv, jobject clazz, jlong self, jint pos)
    {   return (jint)((fjson::Document8_t *)self)->GetObjectSize((uint32_t)pos); }
    JNI_FUNC(jstring, 1GetObjectKey)(JNIEnv *jenv, jobject clazz,
                                     jlong jself, jint pos, jint idx)
    {   fjson::Document8_t *self = (fjson::Document8_t *)jself;
        const char *result = self->GetObjectKey((uint32_t)pos, (uint32_t)idx);
        return jenv->NewStringUTF(result); }
    JNI_FUNC(jint, 1GetObject)(JNIEnv *jenv, jobject clazz, jlong self, jint pos, jint idx)
    {   return (jint)((fjson::Document8_t *)self)->GetObject((uint32_t)pos, (uint32_t)idx); }
    JNI_FUNC(jint, 1SearchObject)(JNIEnv *jenv, jobject clazz,
                                  jlong self, jint pos, jstring jkey)
    {   const char *key = jenv->GetStringUTFChars(jkey, 0);
        uint32_t result = ((fjson::Document8_t *)self)->SearchObject((uint32_t)pos, key);
        if (key) jenv->ReleaseStringUTFChars(jkey, key);
        return (jint)result; }
    JNI_FUNC(jint, 1Locate)(JNIEnv *jenv, jobject clazz, jlong self, jint pos, jstring jpath)
    {   const char *path = jenv->GetStringUTFChars(jpath, 0);
        uint32_t result = ((fjson::Document8_t *)self)->Locate((uint32_t)pos, path);
        if (path) jenv->ReleaseStringUTFChars(jpath, path);
        return (jint)result; }
}
