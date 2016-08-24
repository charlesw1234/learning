#!/bin/bash

PYDIR=/data/python-2.7.12
export LD_LIBRARY_PATH=$PYDIR/lib

$PYDIR/bin/tracd -p 8080 --basic-auth=tractst,tractst/conf/users,localhost tractst
