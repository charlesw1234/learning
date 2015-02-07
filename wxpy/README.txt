This is a standalone build environment for extension of wxpython, the new
wxwidget for wxpython can be compiled and provided as a standalone python
module here.

swig-1.3.29 has to be installed into $(HOME)/usr/bin/swig.
The patch provided by wxPython must be applied before swig-1.3.29 is compiled.

The process of build and install swig-1.3.29 is here:
$ tar xzf swig-1.3.29.tar.gz
$ cd swig-1.3.29
$ patch -p0 < $(path-to-wxpython)/wxPython/SWIG/swig-1.3.29.patch
$ ./configure --prefix=$HOME/usr
$ make -j4
$ make install

Just run 'scons' after the patched swig-1.3.29 is ready.
