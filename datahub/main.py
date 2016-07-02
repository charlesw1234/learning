from random import random
from time import time, sleep
from datahub.config import Config
from datahub.log import Log

class Main(object):
    def __init__(self):
        self.start = time()
        self.config = Config()
        self.log = Log(self.config)

    def exit(self):
        self.log.exit()

    def gensub(self, subname):
        subpid = self.log.fork()
        if subpid == 0: self.subprocess(subname)

    def work(self):
        self.log.progress('main start')
        while self.log.rfds:
            self.log.progress('main(%.1f)' % (time() - self.start))
            self.log.waitpid()
            self.log.select(1)
        self.log.progress('main finish')

    def subprocess(self, subname):
        self.log.progress('%s start' % subname)
        for idx in range(4):
            self.log.exception('%s#%u(%.1f)\n' % (subname, idx, time() - self.start))
            sleep(random())
        self.log.progress('%s finish' % subname)
        self.log.exit()

main = Main()
main.gensub('first')
main.gensub('second')
main.gensub('third')
main.work()
main.exit()
