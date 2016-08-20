#include "com_wl_www_FreezeDocument.h"

extern "C" {
#define JNI_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeDocument_##FUNC
    JNI_FUNC(jint, BodySize)(JNIEnv *jenv, jobject self)
    {
    }
    JNI_FUNC(jboolean, IsFalse)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsTrue)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsInt)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsUint)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsDouble)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsString)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsArray)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jboolean, IsObject)(JNIEnv *jenv, jobject self, jint pos)
    {
    }

    JNI_FUNC(jchar, GetType)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jlong, GetInt)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jlong, GetUint)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jdouble, GetDouble)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jstring, GetString)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jint, GetArraySize)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jint, GetArray)(JNIEnv *jenv, jobject self, jint pos, jint idx)
    {
    }
    JNI_FUNC(jint, GetObjectSize)(JNIEnv *jenv, jobject self, jint pos)
    {
    }
    JNI_FUNC(jstring, GetObjectKey)(JNIEnv *jenv, jobject self, jint pos, jint idx)
    {
    }
    JNI_FUNC(jint, GetObject)(JNIEnv *jenv, jobject self, jint pos, jint idx)
    {
    }
    JNI_FUNC(jint, SearchObject)(JNIEnv *jenv, jobject self, jint pos, jstring key)
    {
    }
    JNI_FUNC(jint, Locate)(JNIEnv *jenv, jobject self, jint pos, jstring path)
    {
    }
}
