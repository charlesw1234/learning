#include "mymodule.hpp"

PyObject *
mymodule_init(void)
{
    PyObject *mod = PyModule_New("mymodule");
    PyModule_AddIntConstant(mod, "myint", 13579);
    return mod;
}
