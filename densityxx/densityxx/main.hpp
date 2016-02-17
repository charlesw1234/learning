#pragma once

#include "densityxx/format.hpp"
#include "densityxx/block.hpp"

namespace density {
    // encode.
    typedef enum {
        ENCODE_STATE_READY = 0,
        ENCODE_STATE_STALL_ON_INPUT,
        ENCODE_STATE_STALL_ON_OUTPUT,
        ENCODE_STATE_ERROR
    } ENCODE_STATE;

    typedef enum {
        ENCODE_PROCESS_WRITE_HEADER,
        ENCODE_PROCESS_WRITE_BLOCKS,
        ENCODE_PROCESS_WRITE_FOOTER,
    } ENCODE_PROCESS;

#pragma pack(push)
#pragma pack(4)
    class encode_state_t {
    public:
        ENCODE_PROCESS process;
        COMPRESSION_MODE compressionMode;
        BLOCK_TYPE blockType;
        const struct stat *fileAttributes;

        uint_fast64_t totalRead;
        uint_fast64_t totalWritten;

        block_encode_state_t *blockEncodeState;

        ENCODE_STATE init(memory_location_t *, const COMPRESSION_MODE, const BLOCK_TYPE);
        ENCODE_STATE continue_(memory_teleport_t *, memory_location_t *);
        ENCODE_STATE finish(memory_teleport_t *, memory_location_t *);
    };
#pragma pack(pop)

    // decode.
#if DENSITY_WRITE_MAIN_FOOTER == DENSITY_YES && DENSITY_ENABLE_PARALLELIZABLE_DECOMPRESSIBLE_OUTPUT == DENSITY_YES
#define DENSITY_DECODE_END_DATA_OVERHEAD   (sizeof(density::main_footer_t))
#else
#define DENSITY_DECODE_END_DATA_OVERHEAD   0
#endif

    typedef enum {
        DECODE_STATE_READY = 0,
        DECODE_STATE_STALL_ON_INPUT,
        DECODE_STATE_STALL_ON_OUTPUT,
        DECODE_STATE_INTEGRITY_CHECK_FAIL,
        DECODE_STATE_ERROR
    } DECODE_STATE;

    typedef enum {
        DECODE_PROCESS_READ_HEADER,
        DECODE_PROCESS_READ_BLOCKS,
        DECODE_PROCESS_READ_FOOTER,
    } DECODE_PROCESS;
    
#pragma pack(push)
#pragma pack(4)
    class decode_state_t {
    public:
        DECODE_PROCESS process;

        uint_fast64_t totalRead;
        uint_fast64_t totalWritten;

        main_header_t header;
        main_footer_t footer;

        block_decode_state_t *blockDecodeState;

        DECODE_STATE init(memory_teleport_t *);
        DECODE_STATE continue_(memory_teleport_t *, memory_location_t *);
        DECODE_STATE finish(memory_teleport_t *, memory_location_t *);
    };
#pragma pack(pop)
}
