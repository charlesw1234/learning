#include "bookfile.hpp"

namespace bookfile {
    bookfile_t::bookfile_t(const char *fname, unsigned num_hashes):
        std::vector<chapter_hash_t>(num_hashes)
    {
        if ((fp = fopen(fname, "wb+"))) {
            tail = 0;
            for (unsigned idx = 0; idx < size() - 1; ++idx) {
                at(idx).next = tail;
                tail += sizeof(chapter_hash_t) / size_block;
            }
        }
    }
    bookfile_t::bookfile_t(const char *fname): std::vector<chapter_hash_t>()
    {
        if ((fp = fopen(fname, "rb+"))) {
            for (uint32_t position = 0; position != UINT32_MAX; position = back().next) {
                push_back(chapter_hash_t());
                fseek(fp, position * size_block, SEEK_SET);
                fread(&back(), 1, sizeof(back()), fp);
            }
            fseek(fp, 0, SEEK_END);
            tail = (unsigned)(ftell(fp) / size_block);
        }
    }
    bookfile_t::~bookfile_t()
    {
        if (fp) {
            unsigned idx = 0;
            for (uint32_t position = 0; position != UINT32_MAX; position = back().next) {
                if (at(idx).magic == magic_dirty) {
                    fseek(fp, position * size_block, SEEK_SET);
                    at(idx).magic = magic_clean;
                    fwrite(&at(idx), 1, sizeof(at(idx)), fp);
                }
                ++idx;
            }
        }
    }

    uint64_t
    bookfile_t::freed_blocks(void)
    {
        uint64_t value = 0;
        for (unsigned idx = 0; idx < size(); ++idx)
            value += at(idx).freed_blocks;
        return value;
    }

    bool
    bookfile_t::insert(uint64_t chapterid, uint32_t blocks)
    {
        unsigned idx;
        chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (cur->chapters[idx0].blank()) { // not found.
                    cur->chapters[idx0].blocks = blocks;
                    cur->chapters[idx0].position = tail;
                    cur->chapters[idx0].chapterid = chapterid;
                    cur->magic = magic_dirty;
                    tail += blocks;
                    return true;
                } else if (cur->chapters[idx0].removed()) { continue;
                } else if (cur->chapters[idx0].chapterid == chapterid) { // found.
                    if (cur->chapters[idx0].blocks > blocks) { // in position.
                        cur->freed_blocks += cur->chapters[idx0].blocks - blocks;
                        cur->chapters[idx0].blocks = blocks;
                        cur->magic = magic_dirty;
                    } else if (cur->chapters[idx0].blocks < blocks) { // append.
                        cur->freed_blocks += cur->chapters[idx0].blocks;
                        cur->chapters[idx0].blocks = blocks;
                        cur->chapters[idx0].position = tail;
                        cur->magic = magic_dirty;
                        tail += blocks;
                    }
                    return true;
                }
            }
        }
        back().next = tail;
        push_back(chapter_hash_t());
        tail += sizeof(chapter_hash_t) / size_block;
        cur = &back();
        cur->chapters[idx1].blocks = blocks;
        cur->chapters[idx1].position = tail;
        cur->chapters[idx1].chapterid = chapterid;
        tail += blocks;
        return true;
    }
    bool
    bookfile_t::remove(uint64_t chapterid)
    {
        chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (cur->chapters[idx0].blank()) return false; // not found.
                else if (cur->chapters[idx0].removed()) continue;
                else if (cur->chapters[idx0].chapterid == chapterid) { // found.
                    cur->freed_blocks += cur->chapters[idx0].blocks;
                    cur->chapters[idx0].blocks = UINT32_MAX;
                    cur->magic = magic_dirty;
                    return true;
                }
            }
        }
        return false;
    }
    bool
    bookfile_t::seek(uint64_t chapterid, uint32_t *blocks)
    {
        chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (cur->chapters[idx0].blank()) return false; // not found.
                else if (cur->chapters[idx0].removed()) continue;
                else if (cur->chapters[idx0].chapterid == chapterid) { // found.
                    *blocks = cur->chapters[idx0].blocks;
                    fseek(fp, cur->chapters[idx0].position * size_block, SEEK_SET);
                    return true;
                }
            }
        }
        return false;
    }
}
