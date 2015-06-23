#include <Python.h>
#include "mymodule.hpp"

void
round(const char *fname)
{
    PyObject *modules, *mod;
    Py_SetPythonHome("/home/wangli/pyroot/usr");
    Py_Initialize();
    printf("GetPythonHome = [%s]\n", Py_GetPythonHome());
    modules = PyImport_GetModuleDict();
    mod = mymodule_init();
    PyDict_SetItemString(modules, "mymodule", mod);
    Py_DECREF(mod);
    if (PyRun_SimpleFile(fopen(fname, "rt"), fname) < 0) {
        PyErr_Print();
    }
    Py_Finalize();
}

int
main(void)
{
    round("tester0.py");
    round("tester1.py");
    return 0;
}
