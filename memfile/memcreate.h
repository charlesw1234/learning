#pragma once

#include <stdio.h>

#ifdef __cplusplus
#define EXTC extern "C"
#else
#define EXTC
#endif


typedef struct {
    char *body;
    size_t cur, size, space;
}  memcreate_t;

EXTC void init_memcreate(memcreate_t *self);
EXTC FILE *fopen_memcreate(memcreate_t *self);
EXTC void free_memcreate(memcreate_t *self);
