#include "beecrypt/aes.h"
#include "beecrypt/blockmode.h"

static const byte key[] = {
    0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7,
    0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF,
};
static const byte iv[] = {
    0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7,
    0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF,
};
int
main(int argc, char *argv[])
{
    aesParam param;
    uint32_t buf[2048];
    FILE *rfp, *wfp;
    rfp = fopen("test.cipher", "rb");
    fread(buf, 1, sizeof(buf), rfp);
    fclose(rfp);
    aesSetup(&param, key, 256, DECRYPT);
    aesSetIV(&param, iv);
    blockDecryptCBC(&aes, &param, buf, buf, sizeof(buf) / aes.blocksize);
    wfp = fopen("test1.plain", "wb");
    fwrite(buf, 1, sizeof(buf), wfp);
    fclose(wfp);
    return 0;
}
