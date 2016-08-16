from fnmatch import fnmatch
from importlib import import_module
from os import walk
from os.path import abspath, dirname, sep as pathsep, splitext
from .base import BaseCommand

class Command(BaseCommand):
    helpstr = 'show this help message.'
    def run(self, arg0, args):
        maxnamelen, cmds, cmdsdir = 0, [], dirname(abspath(__file__))
        for path, dirlist, filelist in walk(cmdsdir):
            import_path = '.'.join(path[len(cmdsdir) :].split(pathsep))
            for fname in filelist:
                if not fnmatch(fname, '*.py'): continue
                if fname in ['__init__.py']: continue
                cmdname = 'commands%s.%s' % (import_path, splitext(fname)[0])
                modobj = import_module(cmdname)
                if not hasattr(modobj, 'Command'): continue
                cmds.append((cmdname[len('commands.'):], modobj.Command))
                if maxnamelen < len(cmds[-1][0]): maxnamelen = len(cmds[-1][0])
        cmds.sort(key = lambda cmdtuple: cmdtuple[0])
        print('Commands:')
        fmt = '%%%us: %%s' % (maxnamelen + 4)
        for cmdname, cmdobj in cmds:
            print(fmt % (cmdname, getattr(cmdobj, 'helpstr', None)))
