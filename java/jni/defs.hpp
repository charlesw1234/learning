#pragma once

#define __STDC_LIMIT_MACROS
#define __STDC_CONSTANT_MACROS
#define __STDC_FORMAT_MACROS
#ifdef WITH_PYTHON
#include <Python.h>
#endif
#include <sys/stat.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef WITH_PYTHON
typedef PyObject PyObject_t;
typedef PyTypeObject PyTypeObject_t;
typedef PyMethodDef PyMethodDef_t;
typedef PyCFunction PyCFunction_t;
typedef PyObject_t *(* PyMemberNoArgs_t)(PyObject_t *);
typedef PyObject_t *(* PyMemberVarArgs_t)(PyObject_t *, PyObject_t *);

static bool
pytypeobject_setup(PyObject_t *mod, PyTypeObject_t *pytypeobject, Py_ssize_t basicsize,
                   const char *modname, const char *fullname,
                   initproc init, destructor dealloc, PyMethodDef_t *methods)
{
    memset(pytypeobject, 0, sizeof(*pytypeobject));
    pytypeobject->tp_name = fullname;
    pytypeobject->tp_basicsize = basicsize;
    pytypeobject->tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
    pytypeobject->tp_init = init;
    pytypeobject->tp_dealloc = dealloc;
    pytypeobject->tp_methods = methods;
    pytypeobject->tp_alloc = PyType_GenericAlloc;
    pytypeobject->tp_new = PyType_GenericNew;
    pytypeobject->tp_free = PyObject_Del;
    if (PyType_Ready(pytypeobject) < 0) return false;
    Py_INCREF(pytypeobject);
    PyModule_AddObject(mod, modname, (PyObject_t *)pytypeobject);
    return true;
}
#endif
