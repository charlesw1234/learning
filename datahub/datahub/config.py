class Config(object):
    def __init__(self):
        self.logfpath = 'test.log'
        self.logopt = {
            'tsfmts': ['%d-%H:%M:%S', '%Y/%m'],
            'lnfmt0': '%(oper)4s@%(now0)s> %(msgln)s\n',
            'lnfmt1': '      %(now1)s#%(idx)02u> %(msgln)s\n',
            'WARN': {},
            'ERR': {},
            'EXC': {},
            'PROG': {},
            'DB': {},
            'STOR': {},
            'SRC': {}
            }
