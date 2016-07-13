#pragma once

#include <stdio.h>

#ifdef __cplusplus
#define EXTC extern "C"
#else
#define EXTC
#endif

EXTC FILE *fopen_memcreate(void **body, size_t *bodysize);
