#pragma once

#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <vector>

namespace bookfile {
    const uint32_t magic_clean = 0xA9C7A7C9;
    const uint32_t magic_dirty = 0xA9C7A7C8;
    const unsigned size_block = 16;
    const unsigned num_chapter_hash = 127;
    const unsigned num_hash_steps = 5;

    class chapter_t { // 16 bytes.
    public:
        uint32_t blocks;
        uint32_t position;
        uint64_t chapterid;

        inline bool blank(void) const { return blocks == 0; }
        inline bool removed(void) const { return blocks == UINT32_MAX; }
        inline bool used(void) const { return blocks != 0 && blocks != UINT32_MAX; }
    };
    class chapter_hash_t { // 2048 bytes.
    public:
        uint32_t magic;
        uint32_t next;
        uint32_t num_chapters;
        uint32_t freed_blocks;
        chapter_t chapters[num_chapter_hash];

        inline chapter_hash_t(bool dirty = true)
        {   magic = magic_dirty; next = UINT32_MAX;
            num_chapters = 0; freed_blocks = 0;
            memset(chapters, 0, sizeof(chapters)); }
    };

    class bookfile_t: public std::vector<chapter_hash_t> {
    public:
        bookfile_t(const char *fname, unsigned num_hashes); // for the first file creation.
        bookfile_t(const char *fname); // to open an exists file.
        ~bookfile_t();

        inline bool usable(void) const { return fp != NULL; }

        inline uint32_t num_chapters(void) const
        {   uint32_t value = 0;
            for (unsigned idx = 0; idx < size(); ++idx) value += at(idx).num_chapters;
            return value; }
        inline uint32_t freed_blocks(void) const
        {   uint32_t value = 0;
            for (unsigned idx = 0; idx < size(); ++idx) value += at(idx).freed_blocks;
            return value; }

        bool insert(uint64_t chapterid, uint32_t blocks);
        bool remove(uint64_t chapterid);

        bool seek(uint64_t chapterid, uint32_t *blocks);
        inline uint32_t read(uint8_t *data, uint32_t blocks)
        {   return fread(data, size_block, blocks, fp); }
        inline uint32_t write(const uint8_t *data, uint32_t blocks)
        {   return fwrite(data, size_block, blocks, fp); }
    private:
        FILE *fp;
        uint32_t tail;
        inline unsigned hashfunc(uint64_t chapterid)
        {   return (unsigned)(chapterid % num_chapter_hash); }
    };
}
