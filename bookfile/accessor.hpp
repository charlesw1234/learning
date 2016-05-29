#pragma once

#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <bzlib.h>
#include <openssl/aes.h>

namespace bookfile {
    // all enoder operations are done in server, provide one pass API only.
    class encoder_t {

    public:
        encoder_t(const uint8_t *secret, const uint8_t *plain, unsigned long bytes);
        ~encoder_t() { free(cipher); }

        inline int get_rc(void) const { return rc; }
        inline unsigned long get_bytes(void) const { return bytes; }
        inline unsigned long get_cbytes(void) const { return cbytes; }
        inline uint32_t get_blocks(void) const { return blocks; }
        inline const uint8_t *get(void) const { return cipher; }
    private:
        int rc;
        unsigned long bytes, cbytes;
        uint32_t blocks;
        uint8_t *cipher;
    };

    class decoder_t {
    public:
        decoder_t(const uint8_t *secret, unsigned long bytes, unsigned long cbytes);
        ~decoder_t();
    private:
        const uint8_t *secret;
        unsigned long bytes, cbytes;
    };
}
