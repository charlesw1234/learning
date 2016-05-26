#include "bookfile.hpp"

namespace bookfile {
    bookfile_t::bookfile_t(const char *fname)
    {
        fp = fopen(fname, "rb+");
        fseek(fp, 0, SEEK_END);
        if (ftell(fp) == 0) {
            chapter_hash_t hash;
            memset(&hash, 0, sizeof(hash));
            hash.magic = magic;
            hash.next = UINT32_MAX;
            fwrite(&hash, 1, sizeof(hash), fp);
        }
    }

    uint64_t
    bookfile_t::freed_blocks(void)
    {
        uint64_t value = 0;
        chapter_hash_t hash;

        for (uint32_t position = 0; position != UINT32_MAX; position = hash.next) {
            fseek(fp, position * size_block, SEEK_SET);
            fread(&hash, 1, sizeof(hash), fp);
            value += hash.freed_blocks;
        }
        return value;
    }

    unsigned
    bookfile_t::next(uint64_t *chapters, uint32_t *position)
    {
        chapter_hash_t hash;
        uint64_t *cur = chapters;

        fseek(fp, *position * size_block, SEEK_SET);
        fread(&hash, 1, sizeof(hash), fp);
        for (unsigned idx = 0; idx < num_chapter_hash; ++idx)
            if (hash.chapters[idx].blocks == 0) continue;
            else if (hash.chapters[idx].blocks == UINT32_MAX) continue;
            else *cur++ = hash.chapters[idx].chapterid;
        *position = hash.next;
        return (unsigned)(cur - chapters);
    }

    bool
    bookfile_t::insert(uint64_t chapterid, uint32_t blocks)
    {
        uint32_t position, tail;
        chapter_hash_t hash;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        fseek(fp, 0, SEEK_END);
        tail = ftell(fp) / size_block;
        for (position = 0; position != UINT32_MAX; position = hash.next) {
            fseek(fp, position * size_block, SEEK_SET);
            fread(&hash, 1, sizeof(hash), fp);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (hash.chapters[idx0].blocks == 0) { // not found.
                    hash.chapters[idx0].blocks = blocks;
                    hash.chapters[idx0].position = tail;
                    hash.chapters[idx0].chapterid = chapterid;
                    fseek(fp, position * size_block, SEEK_SET);
                    fwrite(&hash, 1, sizeof(hash), fp);
                    fseek(fp, hash.chapters[idx0].position * size_block, SEEK_SET);
                    return true;
                } else if (hash.chapters[idx0].blocks == UINT32_MAX) { continue;
                } else if (hash.chapters[idx0].chapterid == chapterid) { // found.
                    if (hash.chapters[idx0].blocks > blocks) { // in position.
                        hash.freed_blocks += hash.chapters[idx0].blocks - blocks;
                        hash.chapters[idx0].blocks = blocks;
                        fseek(fp, position * size_block, SEEK_SET);
                        fwrite(&hash, 1, sizeof(hash), fp);
                    } else if (hash.chapters[idx0].blocks < blocks) { // append.
                        hash.freed_blocks += hash.chapters[idx0].blocks;
                        hash.chapters[idx0].blocks = blocks;
                        hash.chapters[idx0].position = tail;
                        fseek(fp, position * size_block, SEEK_SET);
                        fwrite(&hash, 1, sizeof(hash), fp);
                    }
                    fseek(fp, hash.chapters[idx0].position * size_block, SEEK_SET);
                    return true;
                }
            }
        }
        // update the last hash.
        hash.next = tail;
        fseek(fp, position * size_block, SEEK_SET);
        fwrite(&hash, 1, sizeof(hash), fp);
        // build a new hash as the last hash.
        memset(&hash, 0, sizeof(hash));
        hash.magic = magic;
        hash.next = UINT32_MAX;
        hash.chapters[idx1].blocks = blocks;
        hash.chapters[idx1].position = tail + sizeof(hash) / size_block;
        hash.chapters[idx1].chapterid = chapterid;
        position = tail;
        fseek(fp, position * size_block, SEEK_SET);
        fwrite(&hash, 1, sizeof(hash), fp);
        return true;
    }
    bool
    bookfile_t::search(uint64_t chapterid, uint32_t *blocks)
    {
        chapter_hash_t hash;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (uint32_t position = 0; position != UINT32_MAX; position = hash.next) {
            fseek(fp, position * size_block, SEEK_SET);
            fread(&hash, 1, sizeof(hash), fp);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (hash.chapters[idx0].blocks == 0) return false; // not found.
                else if (hash.chapters[idx0].blocks == UINT32_MAX) continue;
                else if (hash.chapters[idx0].chapterid == chapterid) { // found.
                    fseek(fp, hash.chapters[idx0].position * size_block, SEEK_SET);
                    return true;
                }
            }
        }
        return false;
    }
    bool
    bookfile_t::remove(uint64_t chapterid)
    {
        chapter_hash_t hash;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (uint32_t position = 0; position != UINT32_MAX; position = hash.next) {
            fseek(fp, position * size_block, SEEK_SET);
            fread(&hash, 1, sizeof(hash), fp);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                if (hash.chapters[idx0].blocks == 0) return false; // not found.
                else if (hash.chapters[idx0].blocks == UINT32_MAX) continue;
                else if (hash.chapters[idx0].chapterid == chapterid) { // found.
                    hash.freed_blocks += hash.chapters[idx0].blocks;
                    hash.chapters[idx0].blocks = UINT32_MAX;
                    fseek(fp, position * size_block, SEEK_SET);
                    fwrite(&hash, 1, sizeof(hash), fp);
                    return true;
                }
            }
        }
        return false;
    }
}
