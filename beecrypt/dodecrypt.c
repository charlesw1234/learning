#include "beecrypt/aes.h"
#include "beecrypt/blockmode.h"

static const byte key[] = {
    "--------"
    "--------"
    "--------"
    "--------"    
};
static const byte iv[] = {
    "++++++++"
    "++++++++"
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
