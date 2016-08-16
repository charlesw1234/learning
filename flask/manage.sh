#!/bin/bash

PYDIR=/data/python-3.5.2
export LD_LIBRARY_PATH=$PYDIR/lib

$PYDIR/bin/python3 manage.py $*
