#include "accessor.hpp"

namespace bookfile {
    encoder_t::encoder_t(const uint8_t *secret, const uint8_t *plain, unsigned long bytes)
    {
        this->bytes = bytes;
        blocks = (uint32_t)((bytes + AES_BLOCK_SIZE - 1) / AES_BLOCK_SIZE);
        unsigned destlen = (blocks - 1) * AES_BLOCK_SIZE;
        cipher = (uint8_t *)malloc(blocks * AES_BLOCK_SIZE);
        // try compression.
        rc = BZ2_bzBuffToBuffCompress((char *)cipher, &destlen, (char *)plain, bytes, 9, 0, 0);
        switch (rc) {
        case BZ_OK: // compressed version used.
            cbytes = destlen;
            blocks = (cbytes + AES_BLOCK_SIZE - 1) / AES_BLOCK_SIZE;
            break;
        case BZ_OUTBUFF_FULL: // store directly.
            rc = BZ_OK;
            cbytes = bytes;
            memcpy(cipher, plain, bytes);
            break;
        default: return;
        }
        if (secret == NULL) memset(cipher + cbytes, 0, blocks * AES_BLOCK_SIZE - cbytes);
        else {
            // fill the tail by random to protect the secret.
            for (unsigned pos = cbytes; pos < blocks * AES_BLOCK_SIZE; ++pos)
                cipher[pos] = (uint8_t)random();
            // do the encryption.
            AES_KEY key;
            uint8_t ivec[AES_BLOCK_SIZE];
            AES_set_encrypt_key(secret, 256, &key);
            memcpy(ivec, secret + 256 / 8, AES_BLOCK_SIZE);
            AES_cbc_encrypt(cipher, cipher, blocks * AES_BLOCK_SIZE, &key, ivec, AES_ENCRYPT);
        }
    }

    uint8_t *
    decode(const uint8_t *secret, uint8_t *cipher, unsigned long szcipher,
           unsigned long bytes, unsigned long cbytes)
    {
        uint8_t *plain = (uint8_t *)malloc(bytes);
        uint32_t blocks = (uint32_t)((cbytes + AES_BLOCK_SIZE - 1) / AES_BLOCK_SIZE);
        if (szcipher != blocks * AES_BLOCK_SIZE) { free(plain); return NULL; }
        if (secret != NULL) {
            AES_KEY key;
            uint8_t ivec[AES_BLOCK_SIZE];
            AES_set_decrypt_key(secret, 256, &key);
            memcpy(ivec, secret + 256 / 8, AES_BLOCK_SIZE);
            AES_cbc_encrypt(cipher, cipher, blocks * AES_BLOCK_SIZE, &key, ivec, AES_DECRYPT);
        }
        if (bytes == cbytes) memcpy(plain, cipher, bytes);
        else {
            unsigned destlen = bytes;
            int rc = BZ2_bzBuffToBuffDecompress((char *)plain, &destlen,
                                                (char *)cipher, cbytes, 0, 0);
            if (rc != BZ_OK || destlen != bytes) { free(plain); return NULL; }
        }
        return plain;
    }
}
