#define _GNU_SOURCE
#include <stdlib.h>
#include <string.h>
#include "memcreate.h"

static const size_t pagesize = 4096;
static int
memcreate_size_ensure(memcreate_t *self, size_t newsize, int clean_ornot)
{
    char *newbody = self->body;
    size_t newspace = self->space;
    if (newsize <= self->size) return 0;
    if (newsize > newspace) { // enlarge the allocated space if required.
        newspace += pagesize - newspace % pagesize;
        while (newsize > newspace) newspace += newspace;
        newbody = (char *)realloc(newbody, newspace);
        if (newbody == NULL) return -1;
        self->body = newbody;
        self->space = newspace;
    }
    if (self->size < newsize && clean_ornot)
        memset(self->body + self->size, 0, newsize - self->size);
    self->size = newsize;
    return 0;
}

ssize_t
memcreate_read(void *vself, char *buf, size_t size)
{
    memcreate_t *self = (memcreate_t *)vself;
    size_t read_size = self->size - self->cur;
    if (read_size > size) read_size = size;
    memcpy(buf, self->body + self->cur, read_size);
    self->cur += read_size;
    return (ssize_t)read_size;
}

ssize_t
memcreate_write(void *vself, const char *buf, size_t size)
{
    memcreate_t *self = (memcreate_t *)vself;
    size_t end = self->cur + size;
    if (memcreate_size_ensure(self, end, 0) < 0) return -1;
    memcpy(self->body + self->cur, buf, size);
    self->cur = end;
    return (ssize_t)size;
}

int
memcreate_seek(void *vself, off64_t *offset, int whence)
{
    memcreate_t *self = (memcreate_t *)vself;
    switch (whence) {
    case SEEK_SET: break;
    case SEEK_CUR: *offset += self->cur; break;
    case SEEK_END: *offset += self->size; break;
    default: return -1;
    }
    if (*offset < 0) return -1;
    if (memcreate_size_ensure(self, (size_t)*offset, 1) < 0) return -1;
    self->cur = (size_t)*offset;
    return 0;
}

int memcreate_close(void *vself) { return 0; }

static const cookie_io_functions_t memcreate_io_functions = {
    memcreate_read, memcreate_write, memcreate_seek, memcreate_close
};

void init_memcreate(memcreate_t *self) { memset(self, 0, sizeof(*self)); }

FILE *
fopen_memcreate(memcreate_t *self)
{
    cookie_io_functions_t memcreate_io_functions = {
        .read = memcreate_read,
        .write = memcreate_write,
        .seek = memcreate_seek,
        .close = memcreate_close
    };
    return fopencookie(self, "wb+", memcreate_io_functions);
}

void
free_memcreate(memcreate_t *self)
{
    if (self->body) free(self->body);
    memset(self, 0, sizeof(*self));
}
