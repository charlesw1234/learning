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

    class chapter_t { // 32 bytes.
    public:
        uint32_t blocks;
        uint32_t position;
        uint64_t chapterid;
        uint64_t md5part0;
        uint64_t md5part1;

        inline bool operator == (const chapter_t &other) const
        { return position == other.position; }
        inline bool operator < (const chapter_t &other) const
        { return position < other.position; }
        inline bool operator > (const chapter_t &other) const
        { return position > other.position; }

        inline bool blank(void) const { return blocks == 0; }
        inline bool removed(void) const { return blocks > (uint32_t)INT32_MAX; }
        inline bool used(void) const { return blocks != 0 && blocks <= (uint32_t)INT32_MAX; }
        inline void remove(void) { blocks |= ((uint32_t)INT32_MAX + 1); }
        inline uint32_t removed_blocks(void) const { return blocks & ((uint32_t)INT32_MAX); }

        inline bool compare(const chapter_t *other) const
        {   return md5part0 == other->md5part0 && md5part1 == other->md5part1 &&
                blocks == other->blocks; }
        inline void update(const chapter_t *other)
        {   blocks = other->blocks;
            chapterid = other->chapterid;
            md5part0 = other->md5part0;
            md5part1 = other->md5part1; }
        inline uint32_t update(const chapter_t *other, uint32_t position)
        {   update(other);  this->position = position;  return position + blocks; }
    };
    class chapter_hash_t { // 4096 bytes.
    public:
        uint32_t magic;
        uint32_t next;
        uint32_t num_chapters;
        uint32_t freed_blocks;
        uint64_t unused0;
        uint64_t unused1;
        chapter_t chapters[num_chapter_hash];

        inline chapter_hash_t(bool dirty = true)
        {   magic = magic_dirty; next = UINT32_MAX;
            num_chapters = 0; freed_blocks = 0;
            unused0 = unused1 = 0;
            memset(chapters, 0, sizeof(chapters)); }

        inline void add(void) { ++num_chapters; magic = magic_dirty; }
        inline void add(uint32_t freed_blocks)
        {   ++num_chapters; this->freed_blocks -= freed_blocks; magic = magic_dirty; }
        inline void remove(uint32_t freed_blocks)
        {   --num_chapters; this->freed_blocks += freed_blocks; magic = magic_dirty; }
    };

    class bookfile_t: public std::vector<chapter_hash_t> {
    public:
        bookfile_t(const char *fname, unsigned num_chapters); // for the first file creation.
        bookfile_t(const char *fname); // to open an exists file.
        inline ~bookfile_t() { flush(); }

        // write all dirty chapter_hash_t into file.
        void flush(void);
        inline bool usable(void) const { return fp != NULL; }

        inline uint32_t num_chapters(void) const
        {   uint32_t value = 0;
            for (unsigned idx = 0; idx < size(); ++idx) value += at(idx).num_chapters;
            return value; }
        inline uint32_t freed_blocks(void) const
        {   uint32_t value = 0;
            for (unsigned idx = 0; idx < size(); ++idx) value += at(idx).freed_blocks;
            return value; }

        // return true when the chapter has to be written in future.
        // return false when a md5 matched chapter encounterd.
        bool insert(const chapter_t *chapter);
        // return true when the provided chapter is found and removed.
        // return false when the provided chapter is not found.
        bool remove(uint64_t chapterid);

        // seek the file pointer to the position to read/write the provided chapter.
        // return NULL if the provided chapter is not found.
        const chapter_t *seek(uint64_t chapterid);

        inline uint32_t read(uint8_t *data, uint32_t blocks)
        {   return fread(data, size_block, blocks, fp); }
        inline uint32_t write(const uint8_t *data, uint32_t blocks)
        {   return fwrite(data, size_block, blocks, fp); }

        uint32_t max_removed_blocks(void) const; // for debug only.
        bool sanity(void) const; // for debug only.
    private:
        FILE *fp;
        uint32_t tail;
        inline unsigned hashfunc(uint64_t chapterid)
        {   return (unsigned)(chapterid % num_chapter_hash); }
    };
}
