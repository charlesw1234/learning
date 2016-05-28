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
                if (cur0->blocks < chapter->blocks) continue; // skip the smaller removed.
                if (curfit == NULL) { curfit = cur; cur0fit = cur0; }
                else if (cur0fit->blocks < cur0->blocks) { curfit = cur; cur0fit = cur0; }
            }
        }
    done:
        if (curfit != NULL) { // an available removed space found.
            cur0fit->update(chapter);
            curfit->add(chapter->blocks);
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
}
