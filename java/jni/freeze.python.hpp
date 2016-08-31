#pragma once

namespace fjson {
    class PythonCount_t {
    public:
        uint32_t nnodes, szstrings;
        PythonCount_t(void): nnodes(0), szstrings(0) {}
        void recur_count(PyObject_t *cur)
        {
            ++nnodes;
            if (PyBytes_Check(cur)) {
                szstrings += PyBytes_Size(cur);
            } else if (PyUnicode_Check(cur)) {
                Py_ssize_t len;
                PyUnicode_AsUTF8AndSize(cur, &len);
                szstrings += len + 1;
            } else if (PyTuple_Check(cur)) {
                for (Py_ssize_t idx = 0; idx < PyTuple_Size(cur); ++idx)
                    recur_count(PyTuple_GetItem(cur, idx));
            } else if (PyList_Check(cur)) {
                for (Py_ssize_t idx = 0; idx < PyList_Size(cur); ++idx)
                    recur_count(PyList_GetItem(cur, idx));
            } else if (PyDict_Check(cur)) {
                nnodes += PyDict_Size(cur);
                PyObject_t *pykey, *pyvalue; Py_ssize_t pos = 0;
                while (PyDict_Next(cur, &pos, &pykey, &pyvalue)) {
                    if (PyBytes_Check(pykey)) {
                        szstrings += PyBytes_Size(pykey);
                    } else if (PyUnicode_Check(pykey)) {
                        Py_ssize_t sz;
                        PyUnicode_AsUTF8AndSize(pykey, &sz);
                        szstrings += sz;
                    }
                    recur_count(pyvalue);
                }
            }
        }
    };
    template<typename VALUE_T>class PythonFill_t {
        uint8_t *types; VALUE_T *values; char *strings;
        uint32_t curused, curoffset;
    public:
        PythonFill_t(uint8_t *types, VALUE_T *values, char *strings):
            types(types), values(values), strings(strings), curused(1), curoffset(0) {}
        void recur_fill(PyObject_t *cur, uint32_t curpos)
        {
            if (cur == Py_None) {
                types[curpos] = fjnull; values[curpos].uint_v = 0;
            } else if (cur == Py_False) {
                types[curpos] = fjfalse; values[curpos].uint_v = 0;
            } else if (cur == Py_True) {
                types[curpos] = fjtrue; values[curpos].uint_v = 0;
            } else if (PyLong_Check(cur)) {
                int overflow;
                types[curpos] = fjint;
                values[curpos].int_v = (int64_t)PyLong_AsLongLongAndOverflow(cur, &overflow);
                if (overflow != 0) {
                    types[curpos] = fjuint;
                    values[curpos].uint_v = (uint64_t)PyLong_AsUnsignedLongLong(cur);
                }
            } else if (PyFloat_Check(cur)) {
                types[curpos] = fjdouble; values[curpos].double_v = PyFloat_AsDouble(cur);
            } else if (PyBytes_Check(cur)) {
                uint32_t sz = (uint32_t)PyBytes_Size(cur);
                types[curpos] = fjstring;
                values[curpos].string.offset = curoffset;
                values[curpos].string.len = sz;
                memcpy(strings + curoffset, PyBytes_AsString(cur), sz);
                curoffset += sz;
            } else if (PyUnicode_Check(cur)) {
                Py_ssize_t len; const char *body = PyUnicode_AsUTF8AndSize(cur, &len);
                types[curpos] = fjstring;
                values[curpos].string.offset = curoffset;
                values[curpos].string.len = (uint32_t)len;
                strcpy(strings + curoffset, body);
                curoffset += len + 1;
            } else if (PyTuple_Check(cur)) {
                types[curpos] = fjarray;
                uint32_t subpos = values[curpos].array.start = curused;
                curused += values[curpos].array.space = PyTuple_Size(cur);
                for (Py_ssize_t idx = 0; idx < PyTuple_Size(cur); ++idx)
                    recur_fill(PyTuple_GetItem(cur, idx), subpos++);
            } else if (PyList_Check(cur)) {
                types[curpos] = fjarray;
                uint32_t subpos = values[curpos].array.start = curused;
                curused += values[curpos].array.space = PyList_Size(cur);
                for (Py_ssize_t idx = 0; idx < PyTuple_Size(cur); ++idx)
                    recur_fill(PyList_GetItem(cur, idx), subpos++);
            } else if (PyDict_Check(cur)) {
                types[curpos] = fjobject;
                uint32_t subpos = values[curpos].object.start = curused;
                values[curpos].object.space = PyDict_Size(cur);
                curused += values[curpos].object.space + values[curpos].object.space;
                PyObject_t *pykey, *pyvalue; Py_ssize_t pos = 0;
                while (PyDict_Next(cur, &pos, &pykey, &pyvalue)) {
                    if (PyBytes_Check(pykey)) {
                        uint32_t sz = (uint32_t)PyBytes_Size(cur);
                        types[subpos] = fjstring;
                        values[subpos].string.offset = curoffset;
                        values[subpos++].string.len = sz;
                        memcpy(strings + curoffset, PyBytes_AsString(cur), sz);
                        curoffset += sz;
                    } else if (PyUnicode_Check(pykey)) {
                        Py_ssize_t len; const char *key = PyUnicode_AsUTF8AndSize(pykey, &len);
                        types[subpos] = fjstring;
                        values[subpos].string.offset = curoffset;
                        values[subpos++].string.len = (uint32_t)len;
                        strcpy(strings + curoffset, key);
                        curoffset += len + 1;
                    }
                    recur_fill(pyvalue, subpos++);
                }
                if (values[curpos].object.space > 1) {
                    Sort_t<VALUE_T> sortobj(types, values, strings);
                    sortobj.recur_sort(values[curpos].object.start, 0, 
                                       (int64_t)(values[curpos].object.space - 1));
                }
            }
        }
    };
}
