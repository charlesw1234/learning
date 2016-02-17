#pragma once

#include "densityxx/memory.hpp"

namespace density {
    // header.
#pragma pack(push)
#pragma pack(4)
    class block_header_t {
    public:
        // Previous block's relative start position (parallelizable decompressible output)
        uint32_t previousBlockRelativeStartPosition;
    };
    uint_fast32_t read(memory_location_t *);
    uint_fast32_t write(memory_location_t *);
#pragma pack(pop)

    // mode_marker.
#pragma pack(push)
#pragma pack(4)
    class mode_marker_t {
    public:
        uint8_t activeBlockMode;
        uint8_t reserved;
        uint_fast32_t read(memory_location_t *);
        uint_fast32_t write(memory_location_t *, const COMPRESSION_MODE);
    };
#pragma pack(pop)

    // footer.
#pragma pack(push)
#pragma pack(4)
    class block_footer_t {
    public:
        uint64_t hashsum1;
        uint64_t hashsum2;
        uint_fast32_t read(memory_location_t *);
        uint_fast32_t write(memory_location_t *, const uint_fast64_t, const uint_fast64_t);
    };
#pragma pack(pop)

    // main header.
#pragma pack(push)
#pragma pack(4)
    struct main_header_parameters {
        union {
            uint64_t as_uint64_t;
            uint8_t as_bytes[8];
        };
    };

    class main_header_t {
        uint8_t version[3];
        uint8_t compressionMode;
        uint8_t blockType;
        uint8_t reserved[3];
        main_header_parameters parameters;

        uint_fast32_t read(memory_location_t *);
        uint_fast32_t write(memory_location_t *, const COMPRESSION_MODE, const BLOCK_TYPE,
                            const main_header_parameters);
    };
#pragma pack(pop)

    // main footer.
#pragma pack(push)
#pragma pack(4)
    class main_footer_t {
    public:
        // Previous block's relative start position (parallelizable decompressible output)
        uint32_t previousBlockRelativeStartPosition;
        uint_fast32_t read(memory_location_t *);
        uint_fast32_t write(memory_location_t *, const uint32_t);
    };
#pragma pack(pop)
}
