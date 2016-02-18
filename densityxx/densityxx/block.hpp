#pragma once

#include "densityxx/format.hpp"
#include "densityxx/spookyhash.hpp"

#define DENSITY_PREFERRED_COPY_BLOCK_SIZE  (1 << 19)
#define DENSITY_SPOOKYHASH_SEED_1  (0xabc)
#define DENSITY_SPOOKYHASH_SEED_2  (0xdef)

namespace density {
    // encode.
    typedef enum {
        BLOCK_ENCODE_STATE_READY = 0,
        BLOCK_ENCODE_STATE_STALL_ON_INPUT,
        BLOCK_ENCODE_STATE_STALL_ON_OUTPUT,
        BLOCK_ENCODE_STATE_ERROR
    } BLOCK_ENCODE_STATE;

    typedef enum {
        BLOCK_ENCODE_PROCESS_WRITE_BLOCK_HEADER,
        BLOCK_ENCODE_PROCESS_WRITE_BLOCK_MODE_MARKER,
        BLOCK_ENCODE_PROCESS_WRITE_BLOCK_FOOTER,
        BLOCK_ENCODE_PROCESS_WRITE_DATA,
    } BLOCK_ENCODE_PROCESS;
    
    typedef enum {
        KERNEL_ENCODE_STATE_READY = 0,
        KERNEL_ENCODE_STATE_INFO_NEW_BLOCK,
        KERNEL_ENCODE_STATE_INFO_EFFICIENCY_CHECK,
        KERNEL_ENCODE_STATE_STALL_ON_INPUT,
        KERNEL_ENCODE_STATE_STALL_ON_OUTPUT,
        KERNEL_ENCODE_STATE_ERROR
    } KERNEL_ENCODE_STATE;

#pragma pack(push)
#pragma pack(4)
    class block_encode_state_t {
    public:
        BLOCK_ENCODE_PROCESS process;
        COMPRESSION_MODE targetMode;
        COMPRESSION_MODE currentMode;
        BLOCK_TYPE blockType;

        uint_fast64_t totalRead;
        uint_fast64_t totalWritten;

        // current_block_data.
        uint_fast64_t inStart;
        uint_fast64_t outStart;

        // integrity_data.
        bool update;
        uint8_t *inputPointer;
        spookyhash_context_t context;

        void *kernelEncodeState;

        BLOCK_ENCODE_STATE init(const COMPRESSION_MODE, const BLOCK_TYPE, void *);
        BLOCK_ENCODE_STATE continue_(memory_teleport_t *, memory_location_t *);
        BLOCK_ENCODE_STATE finish(memory_teleport_t *, memory_location_t *);
    protected:
        virtual KERNEL_ENCODE_STATE _init(void *) = 0;
        virtual KERNEL_ENCODE_STATE
        _process(memory_teleport_t *, memory_location_t *, void *) = 0;
        virtual KERNEL_ENCODE_STATE
        _finish(memory_teleport_t *, memory_location_t *, void *) = 0;
    };
#pragma pack(pop)

    // decode.
    typedef enum {
        BLOCK_DECODE_STATE_READY = 0,
        BLOCK_DECODE_STATE_STALL_ON_INPUT,
        BLOCK_DECODE_STATE_STALL_ON_OUTPUT,
        BLOCK_DECODE_STATE_INTEGRITY_CHECK_FAIL,
        BLOCK_DECODE_STATE_ERROR
    } BLOCK_DECODE_STATE;

    typedef enum {
        BLOCK_DECODE_PROCESS_READ_BLOCK_HEADER,
        BLOCK_DECODE_PROCESS_READ_BLOCK_MODE_MARKER,
        BLOCK_DECODE_PROCESS_READ_BLOCK_FOOTER,
        BLOCK_DECODE_PROCESS_READ_DATA,
    } BLOCK_DECODE_PROCESS;

    typedef enum {
        KERNEL_DECODE_STATE_READY = 0,
        KERNEL_DECODE_STATE_INFO_NEW_BLOCK,
        KERNEL_DECODE_STATE_INFO_EFFICIENCY_CHECK,
        KERNEL_DECODE_STATE_STALL_ON_INPUT,
        KERNEL_DECODE_STATE_STALL_ON_OUTPUT,
        KERNEL_DECODE_STATE_ERROR
    } KERNEL_DECODE_STATE;

#pragma pack(push)
#pragma pack(4)
    class block_decode_state_t {
    public:
        BLOCK_DECODE_PROCESS process;
        COMPRESSION_MODE targetMode;
        COMPRESSION_MODE currentMode;
        BLOCK_TYPE blockType;

        uint_fast64_t totalRead;
        uint_fast64_t totalWritten;
        uint_fast8_t endDataOverhead;

        bool readBlockHeaderContent;
        block_header_t lastBlockHeader;
        mode_marker_t lastModeMarker;
        block_footer_t lastBlockFooter;

        // current_block_data.
        uint_fast64_t inStart;
        uint_fast64_t outStart;

        // integrity_data.
        bool update;
        uint8_t *outputPointer;
        spookyhash_context_t context;

        void *kernelDecodeState;

        BLOCK_DECODE_STATE
        init(const COMPRESSION_MODE, const BLOCK_TYPE,
             const main_header_parameters_t, const uint_fast8_t, void *);
        BLOCK_DECODE_STATE continue_(memory_teleport_t *, memory_location_t *);
        BLOCK_DECODE_STATE finish(memory_teleport_t *, memory_location_t *);
    protected:
        virtual KERNEL_DECODE_STATE
        _init(void*, const main_header_parameters_t, const uint_fast8_t) = 0;
        virtual KERNEL_DECODE_STATE
        _process(memory_teleport_t *, memory_location_t *, void*) = 0;
        virtual KERNEL_DECODE_STATE
        _finish(memory_teleport_t *, memory_location_t *, void*) = 0;
    };
}
