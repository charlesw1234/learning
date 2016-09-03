#define WITH_PYTHON
#include "defs.hpp"
#include "freeze.hpp"
#include "freezerender.hpp"

static PyTypeObject_t PyFreeze4Type, PyFreeze8Type, PyFreezeAutoType;

typedef struct { PyObject_HEAD; fjson::Document4_t *freeze; } PyFreeze4_t;
typedef struct { PyObject_HEAD; fjson::Document8_t *freeze; } PyFreeze8_t;
typedef struct { PyObject_HEAD; fjson::DocumentAuto_t *freeze; } PyFreezeAuto_t;

#define PY_DECL_TEMP template<typename PyFreeze_t, class DOC_T>
#define PY_FREEZE4_TEMP <PyFreeze4_t, fjson::Document4_t>
#define PY_FREEZE8_TEMP <PyFreeze8_t, fjson::Document8_t>
#define PY_FREEZE_AUTO_TEMP <PyFreezeAuto_t, fjson::DocumentAuto_t>

#define PY_PROTOTYPE_NOARGS(FUNC)                                       \
    PY_DECL_TEMP static PyObject_t *PyFreeze_##FUNC(PyObject_t *self)
#define PY_PROTOTYPE_VARARGS(FUNC)                                      \
    PY_DECL_TEMP static PyObject_t *PyFreeze_##FUNC(PyObject_t *self, PyObject_t *args)

#define PY_DECL_FREEZE_NOARGS(FUNC)                                     \
    static PyMemberNoArgs_t FUNC##_Freeze4_NoArgs = FUNC PY_FREEZE4_TEMP; \
    static PyMemberNoArgs_t FUNC##_Freeze8_NoArgs = FUNC PY_FREEZE8_TEMP; \
    static PyMemberNoArgs_t FUNC##_FreezeAuto_NoArgs = FUNC PY_FREEZE_AUTO_TEMP
#define PY_DECL_FREEZE_VARARGS(FUNC)                                    \
    static PyMemberVarArgs_t FUNC##_Freeze4_VarArgs = FUNC PY_FREEZE4_TEMP; \
    static PyMemberVarArgs_t FUNC##_Freeze8_VarArgs = FUNC PY_FREEZE8_TEMP; \
    static PyMemberVarArgs_t FUNC##_FreezeAuto_VarArgs = FUNC PY_FREEZE_AUTO_TEMP

PY_DECL_TEMP static int
PyFreeze_Init(PyObject_t *self, PyObject_t *args, PyObject_t *kwargs)
{
    PyObject_t *pydoc; unsigned pos;
    PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (PyTuple_Size(args) == 1 && PyBytes_Check(PyTuple_GetItem(args, 0))) {
        char *pybody; Py_ssize_t size;
        PyBytes_AsStringAndSize(PyTuple_GetItem(args, 0), &pybody, &size);
        uint8_t *body = (uint8_t *)malloc(size);
        memcpy(body, pybody, size);
        pyself->freeze = new DOC_T(body, (uint32_t)size);
    } else if (PyTuple_Size(args) == 1) {
        pyself->freeze = new DOC_T(PyTuple_GetItem(args, 0));
    } else if (PyArg_ParseTuple(args, "OI", &pydoc, &pos)) {
        if (!PyObject_IsInstance(pydoc, (PyObject_t *)pyself->ob_base.ob_type)) {
            PyErr_Format(PyExc_TypeError, "Must be same type.");
            return -1;
        }
        pyself->freeze = new DOC_T(((PyFreeze_t *)pydoc)->freeze, pos);
    } else {
        pyself->freeze = NULL;
        PyErr_Format(PyExc_ValueError, "Unsupport constructor.");
        return -1;
    }
    return 0;
}
static int
PyFreezeAuto_Init(PyObject_t *self, PyObject_t *args, PyObject_t *kwargs)
{
    PyObject_t *pydoc; unsigned pos;
    PyFreezeAuto_t *pyself = (PyFreezeAuto_t *)self;
    if (PyTuple_Size(args) == 1 && PyBytes_Check(PyTuple_GetItem(args, 0))) {
        char *pybody; Py_ssize_t size;
        PyBytes_AsStringAndSize(PyTuple_GetItem(args, 0), &pybody, &size);
        uint8_t *body = (uint8_t *)malloc(size);
        memcpy(body, pybody, size);
        pyself->freeze = new fjson::DocumentAuto_t(body, (uint32_t)size);
    } else if (PyTuple_Size(args) == 1) {
        pyself->freeze = new fjson::DocumentAuto_t(PyTuple_GetItem(args, 0));
    } else if (PyArg_ParseTuple(args, "OI", &pydoc, &pos)) {
        if (PyObject_IsInstance(pydoc, (PyObject_t *)&PyFreezeAutoType)) {
            pyself->freeze = new fjson::DocumentAuto_t(((PyFreezeAuto_t *)pydoc)->freeze, pos);
        } else if (PyObject_IsInstance(pydoc, (PyObject_t *)&PyFreeze4Type)) {
            pyself->freeze = new fjson::DocumentAuto_t(((PyFreeze4_t *)pydoc)->freeze, pos);
        } else if (PyObject_IsInstance(pydoc, (PyObject_t *)&PyFreeze8Type)) {
            pyself->freeze = new fjson::DocumentAuto_t(((PyFreeze8_t *)pydoc)->freeze, pos);
        } else {
            PyErr_Format(PyExc_TypeError, "Must be same type.");
            return -1;
        }
    } else {
        pyself->freeze = NULL;
        PyErr_Format(PyExc_ValueError, "Unsupport constructor.");
        return -1;
    }
    return 0;
}
PY_DECL_TEMP static void
PyFreeze_Dealloc(PyObject_t *self)
{
    PyFreeze_t *pyself = (PyFreeze_t *)self;
    delete pyself->freeze;
}

static inline PyObject_t *_return_none(void) { Py_INCREF(Py_None); return Py_None; }
static inline PyObject_t *_return_bool(bool value)
{   PyObject_t *pyvalue = value ? Py_True: Py_False;
    Py_INCREF(pyvalue); return pyvalue; }

#define PY_IS_FUNC(FUNC)                                        \
    PY_PROTOTYPE_VARARGS(FUNC)                                  \
    {    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self; \
        if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;    \
        return _return_bool(pyself->freeze->FUNC(pos)); }       \
    PY_DECL_FREEZE_VARARGS(PyFreeze_##FUNC)
#define PY_GET_FUNC(FUNC)                                               \
    PY_PROTOTYPE_VARARGS(FUNC)                                          \
    {   unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;          \
        if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;            \
        return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->FUNC(pos)); } \
    PY_DECL_FREEZE_VARARGS(PyFreeze_##FUNC)
#define PY_GETSUB_FUNC(FUNC)                                            \
    PY_PROTOTYPE_VARARGS(FUNC)                                          \
    {   unsigned pos, idx; PyFreeze_t *pyself = (PyFreeze_t *)self;     \
        if (!PyArg_ParseTuple(args, "II", &pos, &idx)) return NULL;     \
        return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->FUNC(pos, idx)); } \
    PY_DECL_FREEZE_VARARGS(PyFreeze_##FUNC)

PY_PROTOTYPE_NOARGS(BodySize)
{
    PyFreeze_t *pyself = (PyFreeze_t *)self;
    return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->BodySize());
}
PY_DECL_FREEZE_NOARGS(PyFreeze_BodySize);

PY_PROTOTYPE_NOARGS(Body)
{
    PyFreeze_t *pyself = (PyFreeze_t *)self;
    return PyBytes_FromStringAndSize((const char *)pyself->freeze->Body(),
                                     (Py_ssize_t)pyself->freeze->BodySize());
}
PY_DECL_FREEZE_NOARGS(PyFreeze_Body);

PY_PROTOTYPE_NOARGS(ValueSize)
{
    PyFreeze_t *pyself = (PyFreeze_t *)self;
    return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->ValueSize());
}
PY_DECL_FREEZE_NOARGS(PyFreeze_ValueSize);

PY_PROTOTYPE_VARARGS(Unfreeze)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    return pyself->freeze->PythonUnfreeze(pos);
}
PY_DECL_FREEZE_VARARGS(PyFreeze_Unfreeze);

PY_PROTOTYPE_VARARGS(Render)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    fjson::Render_t<DOC_T> render(pyself->freeze, pos);
    return PyUnicode_FromString(render.getc());
}
static PyMemberVarArgs_t PyFreeze_Render_Freeze4_VarArgs = PyFreeze_Render PY_FREEZE4_TEMP;
static PyMemberVarArgs_t PyFreeze_Render_Freeze8_VarArgs = PyFreeze_Render PY_FREEZE8_TEMP;
PyObject_t *
PyFreeze_Render_FreezeAuto_VarArgs(PyObject_t *self, PyObject_t *args)
{
    unsigned pos; PyFreezeAuto_t *pyself = (PyFreezeAuto_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    fjson::RenderAuto_t render(pyself->freeze, pos);
    return PyUnicode_FromString(render.getc());
}

PY_IS_FUNC(IsRemoved);
PY_IS_FUNC(IsNull);
PY_IS_FUNC(IsFalse);
PY_IS_FUNC(IsTrue);
PY_IS_FUNC(IsInt);
PY_IS_FUNC(IsUint);
PY_IS_FUNC(IsDouble);
PY_IS_FUNC(IsString);
PY_IS_FUNC(IsArray);
PY_IS_FUNC(IsObject);

PY_PROTOTYPE_VARARGS(GetInt)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    return PyLong_FromLongLong((long long)pyself->freeze->GetInt(pos));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_GetInt);

PY_PROTOTYPE_VARARGS(GetUint)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    return PyLong_FromUnsignedLongLong((unsigned long long)pyself->freeze->GetUint(pos));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_GetUint);

PY_PROTOTYPE_VARARGS(GetDouble)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    return PyFloat_FromDouble(pyself->freeze->GetDouble(pos));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_GetDouble);

PY_PROTOTYPE_VARARGS(GetString)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    return PyUnicode_FromString(pyself->freeze->GetString(pos));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_GetString);

PY_GET_FUNC(GetStringLen);

PY_GET_FUNC(GetArraySpace);
PY_GET_FUNC(GetArraySize);
PY_GETSUB_FUNC(GetArray);

PY_GET_FUNC(GetObjectSpace);
PY_GET_FUNC(GetObjectSize);
PY_PROTOTYPE_VARARGS(GetObjectKey)
{
    unsigned pos, idx; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "II", &pos, &idx)) return NULL;
    return PyUnicode_FromString(pyself->freeze->GetObjectKey(pos, idx));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_GetObjectKey);
PY_GETSUB_FUNC(GetObjectKeyLen);
PY_GETSUB_FUNC(GetObject);

PY_PROTOTYPE_VARARGS(ObjectSearch)
{
    unsigned pos; const char *key; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "Is", &pos, &key)) return NULL;
    return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->ObjectSearch(pos, key));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_ObjectSearch);

PY_PROTOTYPE_VARARGS(Locate)
{
    unsigned pos; const char *path; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "Is", &pos, &path)) return NULL;
    return PyLong_FromUnsignedLong((unsigned long)pyself->freeze->Locate(pos, path));
}
PY_DECL_FREEZE_VARARGS(PyFreeze_Locate);

PY_PROTOTYPE_VARARGS(Remove)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    pyself->freeze->Remove(pos); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_Remove);

PY_PROTOTYPE_VARARGS(SetNull)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    pyself->freeze->SetNull(pos); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetNull);

PY_PROTOTYPE_VARARGS(SetFalse)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    pyself->freeze->SetFalse(pos); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetFalse);

PY_PROTOTYPE_VARARGS(SetTrue)
{
    unsigned pos; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "I", &pos)) return NULL;
    pyself->freeze->SetTrue(pos); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetTrue);

PY_PROTOTYPE_VARARGS(SetInt)
{
    unsigned pos; long long value; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "IL", &pos, &value)) return NULL;
    pyself->freeze->SetInt(pos, value); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetInt);

PY_PROTOTYPE_VARARGS(SetUint)
{
    unsigned pos; unsigned long long value; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "IK", &pos, &value)) return NULL;
    pyself->freeze->SetUint(pos, value); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetUint);

PY_PROTOTYPE_VARARGS(SetDouble)
{
    unsigned pos; double value; PyFreeze_t *pyself = (PyFreeze_t *)self;
    if (!PyArg_ParseTuple(args, "Id", &pos, &value)) return NULL;
    pyself->freeze->SetDouble(pos, value); return _return_none();
}
PY_DECL_FREEZE_VARARGS(PyFreeze_SetDouble);

#define FREEZE_METHOD_NOARGS(NAME, FUNC, STEM)                          \
    { NAME, (PyCFunction_t)FUNC##_##STEM##_NoArgs, METH_NOARGS, NULL }
#define FREEZE_METHOD_VARARGS(NAME, FUNC, STEM)                         \
    { NAME, (PyCFunction_t)FUNC##_##STEM##_VarArgs, METH_VARARGS, NULL }
#define FREEZE_METHODS(STEM)                                            \
    static PyMethodDef_t Py##STEM##_Methods[] = {                       \
        FREEZE_METHOD_NOARGS("BodySize", PyFreeze_BodySize, STEM),      \
        FREEZE_METHOD_NOARGS("Body", PyFreeze_Body, STEM),              \
        FREEZE_METHOD_NOARGS("ValueSize", PyFreeze_ValueSize, STEM),    \
        FREEZE_METHOD_VARARGS("Unfreeze", PyFreeze_Unfreeze, STEM),     \
        FREEZE_METHOD_VARARGS("Render", PyFreeze_Render, STEM),         \
        FREEZE_METHOD_VARARGS("IsRemoved", PyFreeze_IsRemoved, STEM),   \
        FREEZE_METHOD_VARARGS("IsNull", PyFreeze_IsNull, STEM),         \
        FREEZE_METHOD_VARARGS("IsFalse", PyFreeze_IsFalse, STEM),       \
        FREEZE_METHOD_VARARGS("IsTrue", PyFreeze_IsTrue, STEM),         \
        FREEZE_METHOD_VARARGS("IsInt", PyFreeze_IsInt, STEM),           \
        FREEZE_METHOD_VARARGS("IsUint", PyFreeze_IsUint, STEM),         \
        FREEZE_METHOD_VARARGS("IsDouble", PyFreeze_IsDouble, STEM),     \
        FREEZE_METHOD_VARARGS("IsString", PyFreeze_IsString, STEM),     \
        FREEZE_METHOD_VARARGS("IsArray", PyFreeze_IsArray, STEM),       \
        FREEZE_METHOD_VARARGS("IsObject", PyFreeze_IsObject, STEM),     \
        FREEZE_METHOD_VARARGS("GetInt", PyFreeze_GetInt, STEM),         \
        FREEZE_METHOD_VARARGS("GetUint", PyFreeze_GetUint, STEM),       \
        FREEZE_METHOD_VARARGS("GetDouble", PyFreeze_GetDouble, STEM),   \
        FREEZE_METHOD_VARARGS("GetString", PyFreeze_GetString, STEM),   \
        FREEZE_METHOD_VARARGS("GetStringLen", PyFreeze_GetStringLen, STEM), \
        FREEZE_METHOD_VARARGS("GetArraySpace", PyFreeze_GetArraySpace, STEM), \
        FREEZE_METHOD_VARARGS("GetArraySize", PyFreeze_GetArraySize, STEM), \
        FREEZE_METHOD_VARARGS("GetArray", PyFreeze_GetArray, STEM),     \
        FREEZE_METHOD_VARARGS("GetObjectSpace", PyFreeze_GetObjectSpace, STEM), \
        FREEZE_METHOD_VARARGS("GetObjectSize", PyFreeze_GetObjectSize, STEM), \
        FREEZE_METHOD_VARARGS("GetObjectKey", PyFreeze_GetObjectKey, STEM), \
        FREEZE_METHOD_VARARGS("GetObjectKeyLen", PyFreeze_GetObjectKeyLen, STEM), \
        FREEZE_METHOD_VARARGS("GetObject", PyFreeze_GetObject, STEM),   \
        FREEZE_METHOD_VARARGS("ObjectSearch", PyFreeze_ObjectSearch, STEM), \
        FREEZE_METHOD_VARARGS("Locate", PyFreeze_Locate, STEM),         \
        FREEZE_METHOD_VARARGS("Remove", PyFreeze_Remove, STEM),         \
        FREEZE_METHOD_VARARGS("SetNull", PyFreeze_SetNull, STEM),       \
        FREEZE_METHOD_VARARGS("SetFalse", PyFreeze_SetFalse, STEM),     \
        FREEZE_METHOD_VARARGS("SetTrue", PyFreeze_SetTrue, STEM),       \
        FREEZE_METHOD_VARARGS("SetInt", PyFreeze_SetInt, STEM),         \
        FREEZE_METHOD_VARARGS("SetUint", PyFreeze_SetUint, STEM),       \
        FREEZE_METHOD_VARARGS("SetDouble", PyFreeze_SetDouble, STEM),   \
        { NULL, NULL, 0, NULL }                                         \
    }

FREEZE_METHODS(Freeze4);
FREEZE_METHODS(Freeze8);
FREEZE_METHODS(FreezeAuto);

static PyMethodDef_t methods[] = {
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef freezemodule = {
    PyModuleDef_HEAD_INIT, "_freeze", NULL, -1, methods, NULL, NULL, NULL, NULL
};
extern "C" PyMODINIT_FUNC
PyInit__freeze(void)
{
    PyObject_t *mod;

    if ((mod = PyModule_Create(&freezemodule)) == NULL) return NULL;
    if (!pytypeobject_setup(mod, &PyFreeze4Type, sizeof(PyFreeze4_t),
                            "_freeze4", "_freeze._freeze4",
                            PyFreeze_Init PY_FREEZE4_TEMP,
                            PyFreeze_Dealloc PY_FREEZE4_TEMP,
                            PyFreeze4_Methods)) return NULL;
    if (!pytypeobject_setup(mod, &PyFreeze8Type, sizeof(PyFreeze8_t),
                            "_freeze8", "_freeze._freeze8",
                            PyFreeze_Init PY_FREEZE8_TEMP,
                            PyFreeze_Dealloc PY_FREEZE8_TEMP,
                            PyFreeze8_Methods)) return NULL;
    if (!pytypeobject_setup(mod, &PyFreezeAutoType, sizeof(PyFreezeAuto_t),
                            "_freeze_auto", "_freeze._freeze_auto",
                            PyFreezeAuto_Init,
                            PyFreeze_Dealloc PY_FREEZE_AUTO_TEMP,
                            PyFreezeAuto_Methods)) return NULL;
    return mod;
}
