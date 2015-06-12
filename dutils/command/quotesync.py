from distutils.core import Command

class quotesync(Command):
    name = 'quote_sync'
    description = 'update quote data by self defined rsync.'
    user_options = []

    def __init__(self, *args, **kwargs):
        Command.__init__(self, *args, **kwargs)

    def initialize_options(self):
        print('%s.initialize_options' % self.__class__ )

    def finalize_options(self):
        print('%s.finalize_options' % self.__class__)

    def run(self):
        print('%s.run' % self.__class__)

    def sub_commands(self):
        print('%s.sub_commands' % self.__class__)
