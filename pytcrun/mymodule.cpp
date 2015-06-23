#include "mymodule.hpp"

namespace testcase {
    PyObject *
    mymodule_add(PyObject *self, PyObject *args)
    {
        unsigned val0, val1;
        if (!PyArg_ParseTuple(args, "II", &val0, &val1)) return NULL;
        return PyInt_FromLong(val0 + val1);
    }
    static PyMethodDef mymodule_methods[] = {
        { "add", mymodule_add, METH_VARARGS, NULL },
        { NULL, NULL, 0, NULL }
    };
}

PyObject *
mymodule_init(void)
{
    PyObject *mod = Py_InitModule("mymodule", testcase::mymodule_methods);
    PyModule_AddIntConstant(mod, "myint", 13579);
    return mod;
}
