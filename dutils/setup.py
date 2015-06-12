#!/usr/bin/python
from distutils.dist import Distribution as _Distribution
from distutils.core import setup
from command.ccmap import cclist, ccmap

class Distribution(_Distribution):
    def __init__(self, *args, **kwargs):
        _Distribution.__init__(self, *args, **kwargs)

    def print_commands(self):
        std_commands = map(lambda cc: cc.name, cclist)
        is_std = {}
        for cmd in std_commands:
            is_std[cmd] = 1
        max_length = 0
        for cmd in std_commands:
            if len(cmd) > max_length:
                max_length = len(cmd)
        self.print_command_list(std_commands, "Commands", max_length)

    def get_command_class(self, command):
        if command in ccmap: return ccmap[command]
        raise DistutilsModuleError("invalid command '%s'" % command)

setup(distclass = Distribution)
