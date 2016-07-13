#define _GNU_SOURCE
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    void **body;
    size_t *bodysize;
    size_t cur, space;
}  memcreate_cookie_t;

static const size_t pagesize = 4096;
static int
memcreate_extend(memcreate_cookie_t *self, size_t newsize, int clean_ornot)
{
    void *newbody = *self->body;
    size_t newspace = self->space;
    if (newsize <= *self->bodysize) return 0;
    if (newsize > newspace) {
        newspace += pagesize - newspace % pagesize;
        while (newsize > newspace) newspace += pagesize;
        newbody = realloc(newbody, newspace);
        if (newbody == NULL) return -1;
        *self->body = newbody;
        self->space = newspace;
    }
    if (*self->bodysize < newsize && clean_ornot)
        memset((char *)*self->body + *self->bodysize, 0, newsize - *self->bodysize);
    *self->bodysize = newsize;
    return 0;
}

ssize_t
memcreate_read(void *self, char *buf, size_t size)
{
    memcreate_cookie_t *theself = (memcreate_cookie_t *)self;
    size_t read_size = *theself->bodysize - theself->cur;
    if (read_size > size) read_size = size;
    memcpy(buf, (const char *)*theself->body + theself->cur, read_size);
    theself->cur += read_size;
    return (ssize_t)read_size;
}

ssize_t
memcreate_write(void *self, const char *buf, size_t size)
{
    memcreate_cookie_t *theself = (memcreate_cookie_t *)self;
    size_t end = theself->cur + size;
    if (end > *theself->bodysize) memcreate_extend(theself, end, 0);
    memcpy((char *)*theself->body + theself->cur, buf, size);
    theself->cur += size;
    return (ssize_t)size;
}

int
memcreate_seek(void *self, off64_t *offset, int whence)
{
    memcreate_cookie_t *theself = (memcreate_cookie_t *)self;
    switch (whence) {
    case SEEK_SET: break;
    case SEEK_CUR: *offset += theself->cur; break;
    case SEEK_END: *offset += *theself->bodysize; break;
    default: return -1;
    }
    if (*offset < 0) return -1;
    if (*offset > *theself->bodysize)
        if (memcreate_extend(theself, (size_t)*offset, 0) < 0) return -1;
    theself->cur = (size_t)*offset;
    return 0;
}

int memcreate_close(void *self) { free(self); return 0; }

static const cookie_io_functions_t memcreate_io_functions = {
    memcreate_read, memcreate_write, memcreate_seek, memcreate_close
};

FILE *
fopen_memcreate(void **body, size_t *bodysize)
{
    cookie_io_functions_t memcreate_io_functions = {
        .read = memcreate_read,
        .write = memcreate_write,
        .seek = memcreate_seek,
        .close = memcreate_close
    };
    memcreate_cookie_t *self = (memcreate_cookie_t *)malloc(sizeof(memcreate_cookie_t));
    self->body = body;
    self->bodysize = bodysize;
    self->cur = 0;
    self->space = *bodysize;
    return fopencookie(self, "wb+", memcreate_io_functions);
}
