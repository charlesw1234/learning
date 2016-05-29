#include <stdlib.h>
#include "bookfile.hpp"

const unsigned max_blocks = 256;
class tester_t {
public:
    tester_t(void): book("test.book", 128) {}
    ~tester_t() {}

    void add(void);
    void remove(void);
    void update0(void);
    void update1(void);
    void shrink(void);
    void enlarge(void);
private:
    std::vector<bookfile::chapter_t> used;
    std::vector<bookfile::chapter_t> removed;
    bookfile::bookfile_t book;
    inline uint64_t new_chapterid(void) const
    {   unsigned idx0, idx1; uint64_t chapterid;
        do {
            chapterid = (uint64_t)random();
            for (idx0 = 0; idx0 < used.size(); ++idx0)
                if (used[idx0].chapterid == chapterid) break;
            for (idx1 = 0; idx1 < removed.size(); ++idx1)
                if (removed[idx1].chapterid == chapterid) break;
        } while (idx0 < used.size() || idx1 < removed.size());
        return chapterid; }
};

void
tester_t::add(void)
{
    bookfile::chapter_t chapter;
    chapter.blocks = random() % (max_blocks - 1) + 1;
    chapter.chapterid = new_chapterid();
    chapter.md5part0 = (uint64_t)random();
    chapter.md5part1 = (uint64_t)random();
    uint32_t freed_blocks = book.freed_blocks();
    uint32_t max_removed_blocks = book.max_removed_blocks(chapter.chapterid);

    if (!book.insert(&chapter)) {
        fprintf(stderr, "%u: it should be a new chapter.\n", __LINE__);
    } else if (book.num_chapters() != used.size() + 1) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)used.size());
    } else if (max_removed_blocks >= chapter.blocks &&
               book.freed_blocks() != freed_blocks - chapter.blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(), freed_blocks - chapter.blocks);
    } else if (max_removed_blocks < chapter.blocks && book.freed_blocks() != freed_blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(), freed_blocks);
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    } else {
        used.push_back(chapter);
    }
}
void
tester_t::remove(void)
{
    unsigned idx1 = random() % used.size();
    uint32_t freed_blocks = book.freed_blocks();

    if (!book.remove(used[idx1].chapterid)) {
        fprintf(stderr, "%u: remove a chapter failed.\n", __LINE__);
    } else if (book.num_chapters() != used.size() - 1) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)(used.size() - 1));
    } else if (book.freed_blocks() != freed_blocks + used[idx1].blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(),
                (unsigned)(freed_blocks + used[idx1].blocks));
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    } else {
        removed.push_back(used[idx1]);
        used.erase(used.begin() + idx1);
    }
}
void
tester_t::update0(void)
{
    unsigned idx1 = random() % used.size();
    uint32_t freed_blocks = book.freed_blocks();

    if (book.insert(&used[idx1]) == true) {
        fprintf(stderr, "%u: update the unchanged chapter should return false.\n", __LINE__);
    } else if (book.num_chapters() != used.size()) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)used.size());
    } else if (book.freed_blocks() != freed_blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(), (unsigned)freed_blocks);
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    }
}
void
tester_t::update1(void)
{
    unsigned idx1 = random() % used.size();
    uint32_t freed_blocks = book.freed_blocks();

    used[idx1].md5part0 = (uint64_t)random();
    used[idx1].md5part1 = (uint64_t)random();
    if (book.insert(&used[idx1]) == false) {
        fprintf(stderr, "%u: update the changed chapter should return true.\n", __LINE__);
    } else if (book.num_chapters() != used.size()) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)used.size());
    } else if (book.freed_blocks() != freed_blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(), (unsigned)freed_blocks);
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    }
}
void
tester_t::shrink(void)
{
    unsigned idx1 = random() % used.size();
    uint32_t blocks = used[idx1].blocks;
    uint32_t freed_blocks = book.freed_blocks();

    if (blocks < 2) return;
    used[idx1].blocks -= 1 + random() % (blocks - 1);
    if (book.insert(&used[idx1]) == false) {
        fprintf(stderr, "%u: update the changed chapter should return true.\n", __LINE__);
    } else if (book.num_chapters() != used.size()) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)used.size());
    } else if (book.freed_blocks() != freed_blocks + blocks - used[idx1].blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(),
                (unsigned)(freed_blocks + blocks - used[idx1].blocks));
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    }
}
void
tester_t::enlarge(void)
{

    unsigned idx1 = random() % used.size();
    uint32_t freed_blocks = book.freed_blocks();
    uint32_t blocks = used[idx1].blocks;
    uint32_t max_removed_blocks = book.max_removed_blocks(used[idx1].chapterid);

    used[idx1].blocks += random() % (max_blocks - 1) + 1;
    if (book.insert(&used[idx1]) == false) {
        fprintf(stderr, "%u: update the changed chapter should return true.\n", __LINE__);
    } else if (book.num_chapters() != used.size()) {
        fprintf(stderr, "%u: num_chapters(%u != %u)\n", __LINE__,
                (unsigned)book.num_chapters(), (unsigned)used.size());
    } else if (max_removed_blocks >= used[idx1].blocks &&
               book.freed_blocks() != freed_blocks + blocks - used[idx1].blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(),
                (unsigned)(freed_blocks + blocks - used[idx1].blocks));
    } else if (max_removed_blocks < used[idx1].blocks &&
               book.freed_blocks() != freed_blocks + blocks) {
        fprintf(stderr, "%u: freed_blocks(%u != %u)\n", __LINE__,
                (unsigned)book.freed_blocks(), (unsigned)(freed_blocks + blocks));
    } else if (!book.sanity()) {
        fprintf(stderr, "%u: insantiy detected.\n", __LINE__);
    }
}

int
main(void)
{
    unsigned idx;
    tester_t tester;
    for (idx = 0; idx < 512; ++idx) tester.add();
    for (idx = 0; idx < 128; ++idx) tester.remove();
    for (idx = 0; idx < 256; ++idx)
        switch (random() % 4) {
        case 0: tester.update0(); break;
        case 1: tester.update1(); break;
        case 2: tester.shrink(); break;
        case 3: tester.enlarge(); break;
        }
    for (idx = 0; idx < 128; ++idx) tester.add();
    for (idx = 0; idx < 512; ++idx) tester.remove();
    return 0;
}
