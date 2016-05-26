#pragma once

#include <stdint.h>
#include <stdio.h>
#include <string.h>

namespace bookfile {
    const uint32_t magic = 0xA9C7A7C9;
    const unsigned size_block = 16;
    const unsigned num_chapter_hash = 31;
    const unsigned num_hash_steps = 3;

    class chapter_t { // 16 bytes.
    public:
        uint32_t blocks;
        uint32_t position;
        uint64_t chapterid;
    };
    class chapter_hash_t { // 512 bytes.
    public:
        uint32_t magic;
        uint32_t next;
        uint64_t freed_blocks;
        chapter_t chapters[size_block];
    };

    class bookfile_t {
    public:
        bookfile_t(const char *fname);
        ~bookfile_t() { fclose(fp); }

        uint64_t freed_blocks(void);

        inline unsigned first(uint64_t *chapters, uint32_t *position)
        {   *position = 0; return next(chapters, position); }
        unsigned next(uint64_t *chapters, uint32_t *position);

        bool insert(uint64_t chapterid, uint32_t blocks);
        bool search(uint64_t chapterid, uint32_t *blocks);
        bool remove(uint64_t chapterid);

        inline uint32_t read(uint8_t *data, uint32_t blocks)
        {   return fread(data, size_block, blocks, fp); }
        inline uint32_t write(const uint8_t *data, uint32_t blocks)
        {   return fwrite(data, size_block, blocks, fp); }
    private:
        FILE *fp;
        inline unsigned hashfunc(uint64_t chapterid)
        {   return (unsigned)(chapterid % num_chapter_hash); }
    };
}
