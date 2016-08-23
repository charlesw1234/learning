#!/bin/bash

PYDIR=/data/python-2.7.12
export LD_LIBRARY_PATH=$PYDIR/lib

$PYDIR/bin/python2 $*
