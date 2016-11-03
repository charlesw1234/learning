#pragma once

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>

#ifdef FLATTEN_MULTI_SIZE

#ifndef FLATTEN_MAXSIZE_T
#define FLATTEN_MAXSIZE_T uint64_t
#endif
#define FLATTEN_MULTI_SIZE_ONLY(BODY)  BODY

#else // FLATTEN_MULTI_SIZE

#define FLATTEN_MULTI_SIZE_ONLY(BODY)

#endif // FLATTEN_MULTI_SIZE

namespace flatten {
}
