#include "com_wl_www_FreezeJson4Holder.h"
#include "com_wl_www_FreezeJson4Refer.h"
#include "com_wl_www_FreezeJson8Holder.h"
#include "com_wl_www_FreezeJson8Refer.h"
#include "freeze.cpp"

extern "C" {
#define JNI_4H_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson4Holder__##FUNC
#define JNI_4R_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson4Refer__##FUNC
#define JNI_8H_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson8Holder__##FUNC
#define JNI_8R_FUNC(RET, FUNC) JNIEXPORT RET JNICALL Java_com_wl_www_FreezeJson8Refer__##FUNC
}
