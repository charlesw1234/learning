#include "clsexample.hpp"

tstclass::tstclass(unsigned val) { _val = val; }
unsigned tstclass::add(unsigned v0) { return _val + v0; }
unsigned tstclass::sub(unsigned v0) { return _val - v0; }
unsigned tstclass::mul(unsigned v0) { return _val * v0; }
