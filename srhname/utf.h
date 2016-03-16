#pragma once

#include <stdint.h>

typedef uint16_t UTF16;  /* at least 16 bits */
typedef uint8_t  UTF8;   /* typically 8 bits */

#ifdef __cplusplus
#define EXTC extern "C"
#else
#define EXTC
#endif

EXTC void UTF16ToUTF8(UTF16* pUTF16Start, UTF16* pUTF16End, UTF8* pUTF8Start, UTF8* pUTF8End);
EXTC void UTF8ToUTF16(UTF8* pUTF8Start, UTF8* pUTF8End, UTF16* pUTF16Start, UTF16* pUTF16End);
