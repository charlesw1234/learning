#include <algorithm>
#include "bookfile.hpp"

namespace bookfile {
    bookfile_t::bookfile_t(const char *fname, unsigned num_chapters):
        std::vector<chapter_hash_t>
        ((num_chapters * 3 + num_chapter_hash - 1) / num_chapter_hash)
    {
        if ((fp = fopen(fname, "wb+"))) {
            tail = 0;
            for (unsigned idx = 0; idx < size() - 1; ++idx) {
                tail += sizeof(chapter_hash_t) / size_block;
                at(idx).next = tail;
            }
            tail += sizeof(chapter_hash_t) / size_block;
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

    void
    bookfile_t::flush(void)
    {
        uint32_t position;
        if (fp) {
            for (unsigned idx = 0; idx < size(); ++idx) {
                if (at(idx).magic == magic_clean) continue;
                position = idx == 0 ? 0: at(idx - 1).next;
                fseek(fp, position * size_block, SEEK_SET);
                at(idx).magic = magic_clean;
                fwrite(&at(idx), 1, sizeof(at(idx)), fp);
            }
        }
    }

    bool
    bookfile_t::insert(const chapter_t *chapter)
    {
        unsigned idx;
        chapter_t *cur0, *cur0fit;
        chapter_hash_t *cur, *curfit;
        unsigned idx0, idx1 = hashfunc(chapter->chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        cur = curfit = NULL;  cur0 = cur0fit = NULL;
        for (idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                cur0 = cur->chapters + idx0;
                if (cur0->blank()) goto done; // not found.
                else if (cur0->removed()) {} // do nothing is ok here.
                else if (cur0->chapterid != chapter->chapterid) continue; // do not touch it.
                else if (cur0->compare(chapter)) return false; // unchanged chapter found.
                else { // remove the updated chapterid firstly.
                    cur->remove(cur0->blocks);
                    cur0->remove();
                }
                // check the removed space.
                if (cur0->removed_blocks() < chapter->blocks) continue;
                if (curfit == NULL) {
                    curfit = cur; cur0fit = cur0;
                } else if (cur0->removed_blocks() < cur0fit->removed_blocks()) {
                    // use the smallest.
                    curfit = cur; cur0fit = cur0;
                }
            }
        }
    done:
        if (curfit != NULL) { // an available removed space found.
            curfit->add(cur0fit->removed_blocks(), chapter->blocks);
            cur0fit->update(chapter);
        } else if (cur != NULL && cur0->blank()) { // a free hash cell found.
            tail = cur0->update(chapter, tail);
            cur->add();
        } else { // setup a new chapter_hash_t.
            back().next = tail;
            back().magic = magic_dirty;
            push_back(chapter_hash_t());
            tail += sizeof(chapter_hash_t) / size_block;
            tail = back().chapters[idx1].update(chapter, tail);
            back().add();
        }
        return true;
    }
    bool
    bookfile_t::remove(uint64_t chapterid)
    {
        chapter_t *cur0;
        chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                cur0 = cur->chapters + idx0;
                if (cur0->blank()) return false; // not found.
                else if (cur0->removed()) continue;
                else if (cur0->chapterid == chapterid) { // found.
                    cur->remove(cur0->blocks);
                    cur0->remove();
                    return true;
                }
            }
        }
        return false;
    }
    const chapter_t *
    bookfile_t::seek(uint64_t chapterid)
    {
        chapter_t *cur0;
        chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                cur0 = cur->chapters + idx0;
                if (cur0->blank()) return NULL; // not found.
                else if (cur0->removed()) continue; // skip it.
                else if (cur0->chapterid == chapterid) { // found.
                    fseek(fp, cur0->position * size_block, SEEK_SET);
                    return cur0;
                }
            }
        }
        return NULL;
    }

    uint32_t
    bookfile_t::max_removed_blocks(uint64_t chapterid) const
    {
        uint32_t value = 0;
        const chapter_t *cur0;
        const chapter_hash_t *cur;
        unsigned idx0, idx1 = hashfunc(chapterid);
        unsigned idx2 = (idx1 + num_hash_steps) % num_chapter_hash;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            for (idx0 = idx1; idx0 != idx2; idx0 = (idx0 + 1) % num_chapter_hash) {
                cur0 = cur->chapters + idx0;
                if (cur0->blank()) return value;
                else if (cur0->removed() && value < cur0->removed_blocks())
                    value = cur0->removed_blocks();
            }
        }
        return value;
    }
    bool
    bookfile_t::sanity(void) const
    {
        bool succ = true;
        const chapter_t *cur0;
        const chapter_hash_t *cur;
        uint32_t num_chapters, removed_blocks;
        uint32_t tail = sizeof(chapter_hash_t) / size_block * size();
        std::vector<chapter_t> chapters;

        for (unsigned idx = 0; idx < size(); ++idx) {
            cur = &at(idx);
            num_chapters = removed_blocks = 0;
            for (unsigned idx0 = 0; idx0 < num_chapter_hash; ++idx0) {
                cur0 = cur->chapters + idx0;
                if (cur0->blank()) {
                } else if (cur0->removed()) {
                    tail += cur0->removed_blocks();
                    removed_blocks += cur0->removed_blocks();
                    chapters.push_back(*cur0);
                    chapters.back().blocks = chapters.back().removed_blocks();
                } else {
                    tail += cur0->blocks;
                    ++num_chapters;
                    chapters.push_back(*cur0);
                }
            }
            if (num_chapters != cur->num_chapters || removed_blocks != cur->removed_blocks) {
                fprintf(stderr,
                        "MISMATCHED(%u): num_chapters(%u, %u), removed_blocks(%u, %u)\n",
                        idx, (unsigned)num_chapters, (unsigned)cur->num_chapters,
                        (unsigned)removed_blocks, (unsigned)cur->removed_blocks);
                succ = false;
            }
            tail += cur->lost_blocks;
        }
        if (chapters.size() > 1) {
            std::sort(chapters.begin(), chapters.end());
            for (unsigned idx = 0; idx < chapters.size() - 1; ++idx) {
                if (chapters[idx].position + chapters[idx].blocks <= chapters[idx + 1].position)
                    continue;
                fprintf(stderr, "CONFLICTED: %u(%u, %u), %u(%u, %u)\n",
                        (unsigned)chapters[idx].chapterid,
                        (unsigned)chapters[idx].position,
                        (unsigned)chapters[idx].blocks,
                        (unsigned)chapters[idx + 1].chapterid,
                        (unsigned)chapters[idx + 1].position,
                        (unsigned)chapters[idx + 1].blocks);
            }
        }
        if (tail != this->tail) {
            fprintf(stderr, "MISMATCHED: tail(%u, %u)\n", (unsigned)tail, (unsigned)this->tail);
            succ = false;
        }
        return succ;
    }
}
