#pragma once

#include "densityxx/globals.hpp"

namespace density {
    // buffer.
    typedef enum {
        BUFFER_STATE_OK = 0,                                // Everything went alright
        BUFFER_STATE_ERROR_OUTPUT_BUFFER_TOO_SMALL,         // Output buffer size is too small
        BUFFER_STATE_ERROR_DURING_PROCESSING,               // Error during processing
        BUFFER_STATE_ERROR_INTEGRITY_CHECK_FAIL             // Integrity check has failed
    } BUFFER_STATE;

    struct buffer_processing_result_t {
        BUFFER_STATE state;
        uint_fast64_t bytesRead;
        uint_fast64_t bytesWritten;
    };

    buffer_processing_result_t
    buffer_compress(const uint8_t *in, const uint_fast64_t szin,
                    uint8_t* out, const uint_fast64_t szout,
                    const COMPRESSION_MODE compression_mode,
                    const BLOCK_TYPE block_type);
    buffer_processing_result_t
    buffer_decompress(const uint8_t *in, const uint_fast64_t szin,
                      uint8_t *out, const uint_fast64_t szout);

    // stream.
    typedef enum {
        STREAM_STATE_READY = 0,                             // Awaiting further instructions (new action or adding data to the input buffer)
        STREAM_STATE_STALL_ON_INPUT,                        // There is not enough space left in the input buffer to continue
        STREAM_STATE_STALL_ON_OUTPUT,                       // There is not enough space left in the output buffer to continue
        STREAM_STATE_ERROR_OUTPUT_BUFFER_TOO_SMALL,         // Output buffer size is too small
        STREAM_STATE_ERROR_INVALID_INTERNAL_STATE,          // Error during processing
        STREAM_STATE_ERROR_INTEGRITY_CHECK_FAIL             // Integrity check has failed
    } STREAM_STATE;

    struct stream_header_information_t {
        uint8_t majorVersion;
        uint8_t minorVersion;
        uint8_t revision;
        COMPRESSION_MODE compressionMode;
        BLOCK_TYPE blockType;
    };

    class stream_t {
    public:
        stream_t(void);
        ~stream_t();

        STREAM_STATE prepare(const uint8_t *in, const uint_fast64_t sz,
                             uint8_t *out, const uint_fast64_t szout);
        STREAM_STATE update_input(const uint8_t *in, const uint_fast64_t szin);
        STREAM_STATE update_output(uint8_t *out, const uint_fast64_t szout);
        uint_fast64_t output_available_for_use(void) const;

        STREAM_STATE compress_init(const COMPRESSION_MODE mode, const BLOCK_TYPE block_type);
        STREAM_STATE compress_continue(void);
        STREAM_STATE compress_finish(void);

        STREAM_STATE decompress_init(stream_header_information_t *header_information);
        STREAM_STATE decompress_continue(void);
        STREAM_STATE decompress_finish(void);
    };
}
