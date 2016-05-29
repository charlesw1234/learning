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
        if (secret == NULL) {
            memset(cipher + cbytes, 0, blocks * AES_BLOCK_SIZE - cbytes);
            return;
        }
        // fill the tail by random to protect the secret.
        for (unsigned cipherpos = cbytes; cipherpos < blocks * AES_BLOCK_SIZE; ++cipherpos)
            cipher[cipherpos] = (uint8_t)random();
        // do the encryption.
        AES_KEY key;
        uint8_t ivec[AES_BLOCK_SIZE];
        AES_set_encrypt_key(secret, 256, &key);
        memcpy(ivec, secret + 256 / 8, AES_BLOCK_SIZE);
        AES_cbc_encrypt(cipher, cipher, blocks * AES_BLOCK_SIZE, &key, ivec, AES_ENCRYPT);
    }
}
