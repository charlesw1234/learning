/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class com_wl_www_FreezeJson4 */

#ifndef _Included_com_wl_www_FreezeJson4
#define _Included_com_wl_www_FreezeJson4
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Init
 * Signature: (Ljava/lang/String;)J
 */
JNIEXPORT jlong JNICALL Java_com_wl_www_FreezeJson4__1Init__Ljava_lang_String_2
  (JNIEnv *, jobject, jstring);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Init
 * Signature: (Lcom/wl/www/FreezeJson4;I)J
 */
JNIEXPORT jlong JNICALL Java_com_wl_www_FreezeJson4__1Init__Lcom_wl_www_FreezeJson4_2I
  (JNIEnv *, jobject, jobject, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Free
 * Signature: (J)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1Free
  (JNIEnv *, jobject, jlong);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _writeObject
 * Signature: (JLjava/io/ObjectOutputStream;)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1writeObject
  (JNIEnv *, jobject, jlong, jobject);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _readObject
 * Signature: (Ljava/io/ObjectInputStream;)J
 */
JNIEXPORT jlong JNICALL Java_com_wl_www_FreezeJson4__1readObject
  (JNIEnv *, jobject, jobject);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _BodySize
 * Signature: (J)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1BodySize
  (JNIEnv *, jobject, jlong);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Render
 * Signature: (JI)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_wl_www_FreezeJson4__1Render
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsRemoved
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsRemoved
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsNull
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsNull
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsFalse
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsFalse
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsTrue
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsTrue
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsInt
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsInt
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsUint
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsUint
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsDouble
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsDouble
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsString
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsString
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsArray
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsArray
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _IsObject
 * Signature: (JI)Z
 */
JNIEXPORT jboolean JNICALL Java_com_wl_www_FreezeJson4__1IsObject
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetType
 * Signature: (JI)C
 */
JNIEXPORT jchar JNICALL Java_com_wl_www_FreezeJson4__1GetType
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetInt
 * Signature: (JI)J
 */
JNIEXPORT jlong JNICALL Java_com_wl_www_FreezeJson4__1GetInt
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetUint
 * Signature: (JI)J
 */
JNIEXPORT jlong JNICALL Java_com_wl_www_FreezeJson4__1GetUint
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetDouble
 * Signature: (JI)D
 */
JNIEXPORT jdouble JNICALL Java_com_wl_www_FreezeJson4__1GetDouble
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetString
 * Signature: (JI)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_wl_www_FreezeJson4__1GetString
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetArraySpace
 * Signature: (JI)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetArraySpace
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetArraySize
 * Signature: (JI)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetArraySize
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetArray
 * Signature: (JII)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetArray
  (JNIEnv *, jobject, jlong, jint, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetObjectSpace
 * Signature: (JI)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetObjectSpace
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetObjectSize
 * Signature: (JI)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetObjectSize
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetObjectKey
 * Signature: (JII)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_wl_www_FreezeJson4__1GetObjectKey
  (JNIEnv *, jobject, jlong, jint, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _GetObject
 * Signature: (JII)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1GetObject
  (JNIEnv *, jobject, jlong, jint, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SearchObject
 * Signature: (JILjava/lang/String;)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1SearchObject
  (JNIEnv *, jobject, jlong, jint, jstring);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Locate
 * Signature: (JILjava/lang/String;)I
 */
JNIEXPORT jint JNICALL Java_com_wl_www_FreezeJson4__1Locate
  (JNIEnv *, jobject, jlong, jint, jstring);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _Remove
 * Signature: (JI)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1Remove
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetNull
 * Signature: (JI)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetNull
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetFalse
 * Signature: (JI)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetFalse
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetTrue
 * Signature: (JI)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetTrue
  (JNIEnv *, jobject, jlong, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetInt
 * Signature: (JII)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetInt
  (JNIEnv *, jobject, jlong, jint, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetUint
 * Signature: (JII)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetUint
  (JNIEnv *, jobject, jlong, jint, jint);

/*
 * Class:     com_wl_www_FreezeJson4
 * Method:    _SetDouble
 * Signature: (JID)V
 */
JNIEXPORT void JNICALL Java_com_wl_www_FreezeJson4__1SetDouble
  (JNIEnv *, jobject, jlong, jint, jdouble);

#ifdef __cplusplus
}
#endif
#endif
