#include <Python.h>
#include "mymodule.hpp"

void
round(const char *fname)
{
    if (PyRun_SimpleFile(fopen(fname, "rt"), fname) < 0) {
        PyErr_Print();
    }

}

int
main(void)
{
    PyObject *modules, *mod;
    Py_SetPythonHome("/home/wangli/pyroot/usr");
    Py_Initialize();
    if (PyErr_Occurred()) {
        PyErr_Print();
    }
    printf("GetPythonHome = [%s]\n", Py_GetPythonHome());
    modules = PyImport_GetModuleDict();
    mod = mymodule_init();
    PyDict_SetItemString(modules, "mymodule", mod);

    round("tester0.py");
    round("tester1.py");

    Py_Finalize();
    return 0;
}
