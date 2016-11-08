#include "flatten/file.hpp"
#include "flatten/segment.hpp"

int
main(void)
{
    uint8_t space[1024], *last = space + sizeof(space);
    FILE *cfp = fopen("first.bin", "wb+");
    flatten::file_t fobj(cfp);
    flatten::memfile_t mfobj(4096);
    flatten::segment_t<uint32_t> segment(0, 16);
    uint8_t *cur = segment.save<uint32_t, uint32_t>(space, last);
    const uint8_t *ccur = segment.load<uint32_t, uint32_t>(space, last);
    printf("cur = %p, ccur = %p\n", cur, ccur);
    fclose(cfp);
    return 0;
}
