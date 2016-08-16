from importlib import import_module
from os.path import abspath, dirname
from sys import argv, path as syspath

topdir = abspath(dirname(__file__))
syspath.insert(0, topdir)
arg0 = argv.pop(0)
command = argv.pop(0)
moduleobj = import_module('commands.%s' % command)
cmdobj = moduleobj.Command(topdir)
cmdobj.run(arg0, argv)
