#include <Python.h>
#include "bookfile.hpp"
#include "accessor.hpp"

typedef PyObject PyObject_t;
typedef PyTypeObject PyTypeObject_t;
typedef PyMethodDef PyMethodDef_t;
typedef PyCFunction PyCFunction_t;

static PyTypeObject_t PyBookFileType;

typedef struct {
    PyObject_HEAD;
    bookfile::bookfile_t *bookfile;
}   PyBookFile_t;
static int
PyBookFile_Init(PyObject_t *self, PyObject_t *args, PyObject_t *kwargs)
{
    const char *fname;
    unsigned num_chapters = 0;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "s|I", &fname, &num_chapters)) return -1;
    if (num_chapters == 0) pyself->bookfile = new bookfile::bookfile_t(fname);
    else pyself->bookfile = new bookfile::bookfile_t(fname, num_chapters);
    return 0;
}
static void
PyBookFile_Dealloc(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    delete pyself->bookfile;
}

static PyObject_t *
PyBookFile_Flush(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    pyself->bookfile->flush();
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject_t *
PyBookFile_Usable(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    PyObject_t *pyresult = pyself->bookfile->usable() ? Py_True: Py_False;
    Py_INCREF(pyresult);
    return pyresult;
}
static PyObject_t *
PyBookFile_MaxIndex(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    return PyInt_FromLong(pyself->bookfile->size() * bookfile::num_chapter_hash);
}
static PyObject_t *
PyBookFile_At(PyObject_t *self, PyObject_t *args)
{
    unsigned idx;
    bookfile::chapter_hash_t *cur;
    bookfile::chapter_t *cur0;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "I", &idx)) return NULL;
    if (idx >= pyself->bookfile->size() * bookfile::num_chapter_hash) goto none_quit;
    cur = &pyself->bookfile->at(idx / bookfile::num_chapter_hash);
    cur0 = cur->chapters + idx % bookfile::num_chapter_hash;
    if (cur0->blank() || cur0->removed()) goto none_quit;
    return PyInt_FromLong(cur0->chapterid);
 none_quit:
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject_t *
PyBookFile_NumChapters(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    return PyInt_FromLong((long)pyself->bookfile->num_chapters());
}
static PyObject_t *
PyBookFile_RemovedBlocks(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    return PyInt_FromLong((long)pyself->bookfile->removed_blocks());
}
static PyObject_t *
PyBookFile_LostBlocks(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    return PyInt_FromLong((long)pyself->bookfile->lost_blocks());
}
static PyObject_t *
PyBookFile_FreedBlocks(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    return PyInt_FromLong((long)pyself->bookfile->freed_blocks());
}
static PyObject_t *
PyBookFile_Insert(PyObject_t *self, PyObject_t *args)
{
    PyObject_t *pyresult;
    bookfile::chapter_t chapter;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    unsigned blocks, position, chapterid, md5part0, md5part1;
    if (!PyArg_ParseTuple(args, "IIIII", &blocks, &position, &chapterid, &md5part0, &md5part1))
        return NULL;
    chapter.blocks = (uint32_t)blocks;
    chapter.position = (uint32_t)position;
    chapter.chapterid = (uint64_t)chapterid;
    chapter.md5part0 = (uint64_t)md5part0;
    chapter.md5part1 = (uint64_t)md5part1;
    pyresult = pyself->bookfile->insert(&chapter) ? Py_True: Py_False;
    Py_INCREF(pyresult);
    return pyresult;
}
static PyObject_t *
PyBookFile_Remove(PyObject_t *self, PyObject_t *args)
{
    unsigned chapterid;
    PyObject_t *pyresult;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "I", &chapterid)) return NULL;
    pyresult = pyself->bookfile->remove(chapterid) ? Py_True: Py_False;
    Py_INCREF(pyresult);
    return pyresult;
}
static PyObject_t *
PyBookFile_Seek(PyObject_t *self, PyObject_t *args)
{
    unsigned chapterid;
    PyObject_t *pyresult;
    const bookfile::chapter_t *seekout;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "I", &chapterid)) return NULL;
    if ((seekout = pyself->bookfile->seek(chapterid)) == NULL) {
        pyresult = Py_None;
        Py_INCREF(pyresult);
    } else {
        pyresult = PyTuple_New(5);
        PyTuple_SetItem(pyresult, 0, PyInt_FromLong((long)seekout->blocks));
        PyTuple_SetItem(pyresult, 1, PyInt_FromLong((long)seekout->position));
        PyTuple_SetItem(pyresult, 2, PyInt_FromLong((long)seekout->chapterid));
        PyTuple_SetItem(pyresult, 3, PyInt_FromLong((long)seekout->md5part0));
        PyTuple_SetItem(pyresult, 4, PyInt_FromLong((long)seekout->md5part1));
    }
    return pyresult;
}
static PyObject_t *
PyBookFile_Read(PyObject_t *self, PyObject_t *args)
{
    unsigned blocks;
    PyObject_t *pyresult;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "I", &blocks)) return NULL;
    uint8_t *data = (uint8_t *)malloc(blocks * bookfile::size_block);
    blocks = pyself->bookfile->read(data, blocks);
    pyresult = PyString_FromStringAndSize((const char *)data, blocks * bookfile::size_block);
    free(data);
    return pyresult;
}
static PyObject_t *
PyBookFile_Write(PyObject_t *self, PyObject_t *args)
{
    const char *data; int szdata; uint32_t blocks;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "s#", &data, &szdata)) return NULL;
    if (szdata % bookfile::size_block != 0) {
        PyErr_Format(PyExc_ValueError, "the length of data must be multiple of %u.",
                     bookfile::size_block);
        return NULL;
    }
    blocks = (uint32_t)(szdata / bookfile::size_block);
    return PyInt_FromLong((long)pyself->bookfile->write((const uint8_t *)data, blocks));
}
static PyObject_t *
PyBookFile_MaxRemovedBlocks(PyObject_t *self, PyObject_t *args)
{
    unsigned chapterid;
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    if (!PyArg_ParseTuple(args, "I", &chapterid)) return NULL;
    return PyInt_FromLong((long)pyself->bookfile->max_removed_blocks(chapterid));
}
static PyObject_t *
PyBookFile_Sanity(PyObject_t *self)
{
    PyBookFile_t *pyself = (PyBookFile_t *)self;
    PyObject_t *pyresult = pyself->bookfile->sanity() ? Py_True: Py_False;
    Py_INCREF(pyresult);
    return pyresult;
}

static PyMethodDef_t PyBookFile_Methods[] = {
    { "flush", (PyCFunction_t)PyBookFile_Flush, METH_NOARGS, NULL },
    { "usable", (PyCFunction_t)PyBookFile_Usable, METH_NOARGS, NULL },
    { "max_index", (PyCFunction_t)PyBookFile_MaxIndex, METH_NOARGS, NULL },
    { "at", (PyCFunction_t)PyBookFile_At, METH_VARARGS, NULL },
    { "num_chapters", (PyCFunction_t)PyBookFile_NumChapters, METH_NOARGS, NULL },
    { "removed_blocks", (PyCFunction_t)PyBookFile_RemovedBlocks, METH_NOARGS, NULL },
    { "lost_blocks", (PyCFunction_t)PyBookFile_LostBlocks, METH_NOARGS, NULL },
    { "freed_blocks", (PyCFunction_t)PyBookFile_FreedBlocks, METH_NOARGS, NULL },
    { "insert", (PyCFunction_t)PyBookFile_Insert, METH_VARARGS, NULL },
    { "remove", (PyCFunction_t)PyBookFile_Remove, METH_VARARGS, NULL },
    { "seek", (PyCFunction_t)PyBookFile_Seek, METH_VARARGS, NULL },
    { "read", (PyCFunction_t)PyBookFile_Read, METH_VARARGS, NULL },
    { "write", (PyCFunction_t)PyBookFile_Write, METH_VARARGS, NULL },
    { "max_removed_blocks", (PyCFunction_t)PyBookFile_MaxRemovedBlocks, METH_VARARGS, NULL },
    { "sanity", (PyCFunction_t)PyBookFile_Sanity, METH_NOARGS, NULL },
    { NULL, NULL, 0, NULL }
};

static PyObject_t *
PyEncode(PyObject_t *self, PyObject_t *args)
{
    const char *secret; PyObject_t *pysecret;
    const char *plain; int szplain;
    if (!PyArg_ParseTuple(args, "Os#", &pysecret, &plain, &szplain)) return NULL;
    if (pysecret == Py_None) secret = NULL;
    else if (PyString_Check(pysecret)) {
        if (PyString_Size(pysecret) != 48) {
            PyErr_Format(PyExc_ValueError, "secret must be 48 bytes string.");
            return NULL;
        }
        secret = PyString_AsString(pysecret);
    } else {
        PyErr_Format(PyExc_TypeError, "secret must None or 48 bytes string.");
        return NULL;
    }
    bookfile::encoder_t encoder((const uint8_t *)secret,
                                (const uint8_t *)plain, (unsigned)szplain);
    PyObject_t *pyresult = PyTuple_New(4);
    PyTuple_SetItem(pyresult, 0, PyInt_FromLong(encoder.get_rc()));
    PyTuple_SetItem(pyresult, 1, PyInt_FromLong(encoder.get_bytes()));
    PyTuple_SetItem(pyresult, 2, PyInt_FromLong(encoder.get_cbytes()));
    Py_ssize_t szcipher = encoder.get_blocks() * AES_BLOCK_SIZE;
    PyTuple_SetItem(pyresult, 3,
                    PyString_FromStringAndSize((const char *)encoder.get(), szcipher));
    return pyresult;
}
static PyObject_t *
PyDecode(PyObject_t *self, PyObject_t *args)
{
    const char *secret; PyObject_t *pysecret;
    const char *cipher; int szcipher; uint8_t *cipherdup;
    unsigned bytes, cbytes;
    uint8_t *plain;
    if (!PyArg_ParseTuple(args, "Os#II", &pysecret, &cipher, &szcipher, &bytes, &cbytes))
        return NULL;
    if (pysecret == Py_None) secret = NULL;
    else if (PyString_Check(pysecret)) {
        if (PyString_Size(pysecret) != 48) {
            PyErr_Format(PyExc_ValueError, "secret must be 48 bytes string.");
            return NULL;
        }
        secret = PyString_AsString(pysecret);
    } else {
        PyErr_Format(PyExc_TypeError, "secret must None or 48 bytes string.");
        return NULL;
    }
    cipherdup = (uint8_t *)malloc(szcipher);
    memcpy(cipherdup, cipher, szcipher);
    plain = bookfile::decode((const uint8_t *)secret, cipherdup,
                             (unsigned long)szcipher, bytes, cbytes);
    free(cipherdup);
    if (plain == NULL) {
        PyErr_Format(PyExc_ValueError, "decode failed.");
        return NULL;
    }
    PyObject_t *pyresult = PyString_FromStringAndSize((const char *)plain, bytes);
    free(plain);
    return pyresult;
}

static PyMethodDef_t methods[] = {
    { "encode", (PyCFunction_t)PyEncode, METH_VARARGS, NULL },
    { "decode", (PyCFunction_t)PyDecode, METH_VARARGS, NULL },
    { NULL, NULL, 0, NULL }
};

extern "C" PyMODINIT_FUNC
initbookfile(void)
{
    PyObject_t *mod;
    PyTypeObject_t *pytypeobject = &PyBookFileType;

    if (bookfile::size_block != AES_BLOCK_SIZE) {
        PyErr_Format(PyExc_SystemError, "Assert(%u == %u) FAILED!",
                     (unsigned)bookfile::size_block, AES_BLOCK_SIZE);
        return;
    }
    if ((mod = Py_InitModule("bookfile", methods)) == NULL) return;
    memset(pytypeobject, 0, sizeof(*pytypeobject));
    pytypeobject->tp_name = "bookfile.bookfile";
    pytypeobject->tp_basicsize = sizeof(PyBookFile_t);
    pytypeobject->tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE;
    pytypeobject->tp_init = PyBookFile_Init;
    pytypeobject->tp_dealloc = PyBookFile_Dealloc;
    pytypeobject->tp_methods = PyBookFile_Methods;
    pytypeobject->tp_alloc = PyType_GenericAlloc;
    pytypeobject->tp_new = PyType_GenericNew;
    pytypeobject->tp_free = PyObject_Del;
    if (PyType_Ready(pytypeobject) < 0) return;
    Py_INCREF(pytypeobject);
    PyModule_AddObject(mod, "bookfile", (PyObject_t *)pytypeobject);
}
