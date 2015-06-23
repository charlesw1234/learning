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
    Py_SetPythonHome("/home/wangli/pyroot/usr");
    Py_Initialize();
    if (PyErr_Occurred()) {
        PyErr_Print();
    }
    printf("GetPythonHome = [%s]\n", Py_GetPythonHome());
    mymodule_init();

    round("tester0.py");
    round("tester1.py");

    Py_Finalize();
    return 0;
}
