#pragma once

#include "rapidjson/document.h"

std::string shvalue(const rapidjson::Value *value);
void sharray(FILE *wfp, unsigned indent, const rapidjson::Value &value);
void shobject(FILE *wfp, unsigned indent, const rapidjson::Value &value);
