#include "scanner.hpp"

JNIEXPORT scanner::Scanner_t *
scanner_init(JNIEnv *env, jobject clazz, jstring jfpath)
{
    const char *fpath = (*env)->GetStringUTFChars(env, jfpath, 0);
    return new scanner::Scanner_t(fpath);
}
JNIEXPORT void
scanner_finalizer(JNIEnv *env, jobject clazz, scanner::Scanner_t *sobj)
{
    delete sobj;
}
JNIEXPORT jstring
scanner_scan(JNIEnv *env, jobject clazz, scanner::Scanner_t *sobj, jstring jkeyword)
{
    const char *keyword = (*env)->GetStringUTFChars(env, jkeyword, 0);
    return (*env)->NewStringUTF(env, sobj->scan(keyword));
}

static JNINativeMethod methods[] = {
    { "init", "(Ljava/lang/String)I", (void *)scanner_init },
    { "finalizer", "(I)V", (void *)scanner_finalizer },
    { "scan", "(ILjava/lang/String)Ljava/lang/String", (void *)scanner_scan }
};
static int nummethods = sizeof(methods) / sizeof(methods[0]);

static int
registerNativeMethods(JNIEnv *env, const char *className,
                      JNINativeMethod *gMethods, int numMethods)
{
    jclass clazz = env->FindClass(className);
    if (clazz == NULL) {
        //LOGE("Native registration unable to find class '%s'", className);
        return JNI_FALSE;
    }
    if (env->RegisterNatives(clazz, gMethods, numMethods) < 0) {
        //LOGE("RegisterNatives failed for '%s'", className);
        return JNI_FALSE;
    }
    return JNI_TRUE;
}

typedef union {
    JNIEnv* env;
    void* venv;
} UnionJNIEnvToVoid;

/* This function will be call when the library first be loaded */ 
jint JNI_OnLoad(JavaVM *vm, void *reserved)
{
    UnionJNIEnvToVoid uenv;
    JNIEnv *env = NULL;
    //LOGI("JNI_OnLoad!");

    if (vm->GetEnv((void**)&uenv.venv, JNI_VERSION_1_4) != JNI_OK) {
        //LOGE("ERROR: GetEnv failed");
        return -1;
    }
    env = uenv.env;
    //jniRegisterNativeMethods(env, "whf/jnitest/Person", methods, sizeof(methods) / sizeof(methods[0]));
    if (registerNativeMethods(env, "", methods, nummethods) != JNI_TRUE) {
        //LOGE("ERROR: registerNatives failed");
        return -1;
    }
    return JNI_VERSION_1_4;
}
