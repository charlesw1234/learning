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
    rfp = fopen("test0.plain", "rb");
    fread(buf, 1, sizeof(buf), rfp);
    fclose(rfp);
    aesSetup(&param, key, 256, ENCRYPT);
    aesSetIV(&param, iv);
    blockEncryptCBC(&aes, &param, buf, buf, sizeof(buf) / aes.blocksize);
    wfp = fopen("test.cipher", "wb");
    fwrite(buf, 1, sizeof(buf), wfp);
    fclose(wfp);
    return 0;
}
