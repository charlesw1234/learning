/*
 * Centaurean SpookyHash
 *
 * Copyright (c) 2015, Guillaume Voirin
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of Centaurean nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * 24/01/15 22:32
 *
 * ----------
 * SpookyHash
 * ----------
 *
 * Author(s)
 * Bob Jenkins (http://burtleburtle.net/bob/hash/spooky.html)
 *
 * Description
 * Very fast non cryptographic hash
 */

#ifndef SPOOKYHASH_H
#define SPOOKYHASH_H

#include "context.h"
#include <string.h>

#define SPOOKYHASH_ALLOW_UNALIGNED_READS   1
#define SPOOKYHASH_ROTATE(x, k) (((x) << (k)) | (((x) >> (64 - (k)))))

void spookyhash_128(const void *, size_t, uint64_t *, uint64_t *);

uint64_t spookyhash_64(const void *, size_t, uint64_t);

uint32_t spookyhash_32(const void *, size_t, uint32_t);

void spookyhash_update(spookyhash_context *, const void *, size_t);

void spookyhash_final(spookyhash_context *, uint64_t *, uint64_t *);

void spookyhash_mix(const uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *);

void spookyhash_end_partial(uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *);

void spookyhash_end(const uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *, uint64_t *);

void spookyhash_short_mix(uint64_t *, uint64_t *, uint64_t *, uint64_t *);

void spookyhash_short_end(uint64_t *, uint64_t *, uint64_t *, uint64_t *);

void spookyhash_short(const void *, size_t, uint64_t *, uint64_t *);

#endif
