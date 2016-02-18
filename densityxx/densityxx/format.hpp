#pragma once

#include "densityxx/memory.hpp"

namespace density {
    // header.
#pragma pack(push)
#pragma pack(4)
    class block_header_t {
    public:
        // Previous block's relative start position (parallelizable decompressible output)
        uint32_t relativePosition; // previousBlockRelativeStartPosition
        inline uint_fast32_t read(memory_location_t *in)
        {   in->read(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out)
        {   out->write(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out, const uint32_t relativePosition)
        {   this->relativePosition = relativePosition; return write(out); }
    };
#pragma pack(pop)

    // mode_marker.
#pragma pack(push)
#pragma pack(4)
    class mode_marker_t {
    public:
        uint8_t mode; // activeBlockMode
        uint8_t reserved;
        inline uint_fast32_t read(memory_location_t *in)
        {   in->read(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out)
        {   out->write(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out, const COMPRESSION_MODE mode)
        {   this->mode = mode; return write(out); }
    };
#pragma pack(pop)

    // footer.
#pragma pack(push)
#pragma pack(4)
    class block_footer_t {
    public:
        uint64_t hashsum1;
        uint64_t hashsum2;
        inline uint_fast32_t read(memory_location_t *in)
        {   in->read(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out)
        {   out->write(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t
        write(memory_location_t *out, uint64_t hashsum1, uint64_t hashsum2)
        {   this->hashsum1 = hashsum1; this->hashsum2 = hashsum2; return write(out); }
    };
#pragma pack(pop)

    // main header.
#pragma pack(push)
#pragma pack(4)
    struct main_header_parameters_t {
        union {
            uint64_t as_uint64_t;
            uint8_t as_bytes[8];
        };
    };
    class main_header_t {
    public:
        uint8_t version[3];
        uint8_t compressionMode;
        uint8_t blockType;
        uint8_t reserved[3];
        main_header_parameters_t parameters;

        inline uint_fast32_t read(memory_location_t *in)
        {   in->read(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out)
        {   out->write(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t
        write(memory_location_t *out, const COMPRESSION_MODE compressionMode,
              const BLOCK_TYPE blockType, const main_header_parameters_t parameters)
        {   version[0] = DENSITYXX_MAJOR_VERSION;
            version[1] = DENSITYXX_MINOR_VERSION;
            version[2] = DENSITYXX_REVISION;
            this->compressionMode = compressionMode;
            this->blockType = blockType;
            this->parameters = parameters;
            return write(out); }
    };
#pragma pack(pop)

    // main footer.
#pragma pack(push)
#pragma pack(4)
    class main_footer_t {
    public:
        // Previous block's relative start position (parallelizable decompressible output)
        uint32_t relativePosition; // previousBlockRelativeStartPosition;
        inline uint_fast32_t read(memory_location_t *in)
        {   in->read(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out)
        {   out->write(this, sizeof(*this)); return sizeof(*this); }
        inline uint_fast32_t write(memory_location_t *out, const uint32_t relativePosition)
        {   this->relativePosition = relativePosition; return write(out); }
    };
#pragma pack(pop)
}
