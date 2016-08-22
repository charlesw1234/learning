#include "com_wl_www_FreezeJson4Holder.h"
#include "com_wl_www_FreezeJson4Refer.h"
#include "com_wl_www_FreezeJson8Holder.h"
#include "com_wl_www_FreezeJson8Refer.h"
#include "freeze.cpp"

extern "C" {
#define JNI_4H_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson4Holder__##FUNC
#define JNI_8H_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson8Holder__##FUNC
#define JNI_4R_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson4Refer__##FUNC
#define JNI_8R_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson8Refer__##FUNC
#define JHOLDER2SELF4(JENV, JOTHER)                                     \
    jfieldID fieldid = (JENV)->GetFieldID((JENV)->GetObjectClass(JOTHER), "self", "L"); \
    fjson::Document4_t *self = (fjson::Document4_t *)(JENV)->GetLongField((JOTHER), fieldid)
#define JHOLDER2SELF8(JENV, JOTHER)                                     \
    jfieldID fieldid = (JENV)->GetFieldID((JENV)->GetObjectClass(JOTHER), "self", "L"); \
    fjson::Document8_t *self = (fjson::Document8_t *)(JENV)->GetLongField((JOTHER), fieldid)

    // Holder members.
    JNI_4H_FUNC(jlong, 1Init__Ljava_lang_String_2)
    (JNIEnv *jenv, jobject jclazz, jstring jdocstr)
    {   rapidjson::Document rdoc;
        const char *docstr = jenv->GetStringUTFChars(jdocstr, 0);
        bool haserror = rdoc.Parse<0>(docstr).HasParseError();
        if (docstr) jenv->ReleaseStringUTFChars(jdocstr, docstr);
        return haserror ? 0: (jlong)new fjson::Document4_t(&rdoc); }
    JNI_8H_FUNC(jlong, 1Init__Ljava_lang_String_2)
    (JNIEnv *jenv, jobject jclazz, jstring jdocstr)
    {   rapidjson::Document rdoc;
        const char *docstr = jenv->GetStringUTFChars(jdocstr, 0);
        bool haserror = rdoc.Parse<0>(docstr).HasParseError();
        if (docstr) jenv->ReleaseStringUTFChars(jdocstr, docstr);
        return haserror ? 0: (jlong)new fjson::Document8_t(&rdoc); }

    JNI_4H_FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson4Holder_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jint jpos)
    {   jfieldID fieldid = jenv->GetFieldID(jenv->GetObjectClass(jother), "self", "L");
        fjson::Document4_t *other = (fjson::Document4_t *)jenv->GetLongField(jother, fieldid);
        return (jlong)new fjson::Document4_t(other, (uint32_t)jpos); }
    JNI_8H_FUNC(jlong, 1Init__Lcom_wl_www_FreezeJson8Holder_2I)
    (JNIEnv *jenv, jobject jclazz, jobject jother, jint jpos)
    {   jfieldID fieldid = jenv->GetFieldID(jenv->GetObjectClass(jother), "self", "L");
        fjson::Document8_t *other = (fjson::Document8_t *)jenv->GetLongField(jother, fieldid);
        return (jlong)new fjson::Document8_t(other, (uint32_t)jpos); }

    JNI_4H_FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself)
    {   delete (fjson::Document4_t *)jself; }
    JNI_8H_FUNC(void, 1Free)(JNIEnv *jenv, jobject jclazz, jlong jself)
    {   delete (fjson::Document8_t *)jself; }

    JNI_4H_FUNC(void, 1writeObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jobject jstream)
    {   // FIXME.
        jclass jstream_class = jenv->GetObjectClass(jstream);
        jmethodID methodid0 = jenv->GetMethodID(jstream_class, "write", "(I)V");
        jmethodID methodid1 = jenv->GetMethodID(jstream_class, "write", "(II)V");
        fjson::Document4_t *self = (fjson::Document4_t *)jself;
        size_t size = self->BodySize();
        jenv->CallVoidMethod(jstream, methodid0, (jint)size);
        jbyteArray jbytearray = jenv->NewByteArray(size);
        jenv->SetByteArrayRegion(jbytearray, 0, size, (const jbyte *)self->Body());
        jenv->CallVoidMethod(jstream, methodid1, jbytearray, 0, size);
        jenv->DeleteLocalRef(jbytearray);
    }
    JNI_8H_FUNC(void, 1writeObject)(JNIEnv *jenv, jobject jclazz, jlong jself, jobject jstream)
    {   // FIXME.
        jclass jstream_class = jenv->GetObjectClass(jstream);
        jmethodID methodid0 = jenv->GetMethodID(jstream_class, "write", "(I)V");
        jmethodID methodid1 = jenv->GetMethodID(jstream_class, "write", "([BII)V");
        fjson::Document8_t *self = (fjson::Document8_t *)jself;
        size_t size = self->BodySize();
        jenv->CallVoidMethod(jstream, methodid0, (jint)size);
        jbyteArray jbytearray = jenv->NewByteArray(size);
        jenv->SetByteArrayRegion(jbytearray, 0, size, (const jbyte *)self->Body());
        jenv->CallVoidMethod(jstream, methodid1, jbytearray, 0, size);
        jenv->DeleteLocalRef(jbytearray);
    }

    JNI_4H_FUNC(jlong, 1readObject)(JNIEnv *jenv, jobject jclazz, jobject jstream)
    {   // FIXME.
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
        fjson::Document4_t *self = new fjson::Document4_t(body, size);
        return (jlong)self;
    }
    JNI_8H_FUNC(jlong, 1readObject)(JNIEnv *jenv, jobject jclazz, jobject jstream)
    {   // FIXME.
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
        fjson::Document8_t *self = new fjson::Document8_t(body, size);
        return (jlong)self;
    }
    JNI_4H_FUNC(jint, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
    {   fjson::Document4_t *self = (fjson::Document4_t *)jself;
        return (jint)self->BodySize(); }
    JNI_8H_FUNC(jint, 1BodySize)(JNIEnv *jenv, jobject jclazz, jlong jself)
    {   fjson::Document8_t *self = (fjson::Document8_t *)jself;
        return (jint)self->BodySize(); }

    // Refer members.
    JNI_4R_FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsNull((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsNull)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsNull((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsFalse((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsFalse)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsFalse((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsTrue((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsTrue)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsTrue((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsInt((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsInt)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsInt((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsUint((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsUint)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsUint((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsString((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsString)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsString((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsArray((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsArray)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsArray((uint32_t)jpos); }

    JNI_4R_FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jboolean)self->IsObject((uint32_t)jpos); }
    JNI_8R_FUNC(jboolean, 1IsObject)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jboolean)self->IsObject((uint32_t)jpos); }

    JNI_4R_FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jchar)self->GetType((uint32_t)jpos); }
    JNI_8R_FUNC(jchar, 1GetType)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jchar)self->GetType((uint32_t)jpos); }

    JNI_4R_FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jlong)self->GetInt((uint32_t)jpos); }
    JNI_8R_FUNC(jlong, 1GetInt)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jlong)self->GetInt((uint32_t)jpos); }

    JNI_4R_FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jlong)self->GetUint((uint32_t)jpos); }
    JNI_8R_FUNC(jlong, 1GetUint)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jlong)self->GetUint((uint32_t)jpos); }

    JNI_4R_FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jdouble)self->GetDouble((uint32_t)jpos); }
    JNI_8R_FUNC(jdouble, 1GetDouble)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jdouble)self->GetDouble((uint32_t)jpos); }

    JNI_4R_FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder);
        return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }
    JNI_8R_FUNC(jstring, 1GetString)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder);
        return jenv->NewStringUTF(self->GetString((uint32_t)jpos)); }

    JNI_4R_FUNC(jint, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jint)self->GetArraySize((uint32_t)jpos); }
    JNI_8R_FUNC(jint, 1GetArraySize)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jint)self->GetArraySize((uint32_t)jpos); }

    JNI_4R_FUNC(jint, 1GetArray)(JNIEnv *jenv, jobject jclazz,
                                 jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF4(jenv, jholder);
        return (jint)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }
    JNI_8R_FUNC(jint, 1GetArray)(JNIEnv *jenv, jobject jclazz,
                                 jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF8(jenv, jholder);
        return (jint)self->GetArray((uint32_t)jpos, (uint32_t)jidx); }

    JNI_4R_FUNC(jint, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF4(jenv, jholder); return (jint)self->GetObjectSize((uint32_t)jpos); }
    JNI_8R_FUNC(jint, 1GetObjectSize)(JNIEnv *jenv, jobject jclazz, jobject jholder, jint jpos)
    {   JHOLDER2SELF8(jenv, jholder); return (jint)self->GetObjectSize((uint32_t)jpos); }

    JNI_4R_FUNC(jstring, 1GetObjectKey)(JNIEnv *jenv, jobject jclazz,
                                        jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF4(jenv, jholder);
        return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }
    JNI_8R_FUNC(jstring, 1GetObjectKey)(JNIEnv *jenv, jobject jclazz,
                                        jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF8(jenv, jholder);
        return jenv->NewStringUTF(self->GetObjectKey((uint32_t)jpos, (uint32_t)jidx)); }

    JNI_4R_FUNC(jint, 1GetObject)(JNIEnv *jenv, jobject jclazz,
                                  jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF4(jenv, jholder);
        return (jint)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }
    JNI_8R_FUNC(jint, 1GetObject)(JNIEnv *jenv, jobject jclazz,
                                  jobject jholder, jint jpos, jint jidx)
    {   JHOLDER2SELF8(jenv, jholder);
        return (jint)self->GetObject((uint32_t)jpos, (uint32_t)jidx); }

    JNI_4R_FUNC(jint, 1SearchObject)(JNIEnv *jenv, jobject jclazz,
                                     jobject jholder, jint jpos, jstring jkey)
    {   JHOLDER2SELF4(jenv, jholder);
        const char *key = jenv->GetStringUTFChars(jkey, 0);
        uint32_t result = self->SearchObject((uint32_t)jpos, key);
        if (key) jenv->ReleaseStringUTFChars(jkey, key);
        return (jint)result; }
    JNI_8R_FUNC(jint, 1SearchObject)(JNIEnv *jenv, jobject jclazz,
                                     jobject jholder, jint jpos, jstring jkey)
    {   JHOLDER2SELF8(jenv, jholder);
        const char *key = jenv->GetStringUTFChars(jkey, 0);
        uint32_t result = self->SearchObject((uint32_t)jpos, key);
        if (key) jenv->ReleaseStringUTFChars(jkey, key);
        return (jint)result; }

    JNI_4R_FUNC(jint, 1Locate)(JNIEnv *jenv, jobject jclazz,
                               jobject jholder, jint jpos, jstring jpath)
    {   JHOLDER2SELF4(jenv, jholder);
        const char *path = jenv->GetStringUTFChars(jpath, 0);
        uint32_t result = self->Locate((uint32_t)jpos, path);
        if (path) jenv->ReleaseStringUTFChars(jpath, path);
        return (jint)result; }
    JNI_8R_FUNC(jint, 1Locate)(JNIEnv *jenv, jobject jclazz,
                               jobject jholder, jint jpos, jstring jpath)
    {   JHOLDER2SELF8(jenv, jholder);
        const char *path = jenv->GetStringUTFChars(jpath, 0);
        uint32_t result = self->SearchObject((uint32_t)jpos, path);
        if (path) jenv->ReleaseStringUTFChars(jpath, path);
        return (jint)result; }
}
