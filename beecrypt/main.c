#include "beecrypt/aes.h"
#include "beecrypt/sha384.h"

int main(void)
{
    printf("aesSetup: %p\n", aesSetup);
    printf("aesEncrypt: %p\n", aesEncrypt);
    printf("sha384Update: %p\n", sha384Update);
    return 0;
}
