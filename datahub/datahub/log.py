from datetime import datetime
from os import close as osclose, read as osread
from os import fdopen, fork, getpid, pipe, waitpid, WNOHANG
from select import select
from sys import exit as sysexit
from traceback import format_exc

class Log(object):
    def __init__(self, config):
        self.wfopen = (config.logfpath, 'wt')
        self.wfobj = None
        self.jdesc = config.logopt
        self.rfds = {}

    def wfwrite(self, body):
        if self.wfobj is None: self.wfobj = open(*self.wfopen)
        return self.wfobj.write(body)

    def wfflush(self):
        if self.wfobj is None: return
        self.wfobj.flush()

    def wfclose(self):
        if self.wfobj is None: return
        self.wfobj.close()
        self.wfobj = None

    def fork(self):
        rfd, wfd = pipe()
        subpid = fork()
        if subpid == 0: # subprocess.
            del(self.rfds)
            osclose(rfd)
            self.wfclose()
            self.wfobj = fdopen(wfd, 'wt')
            return subpid
        osclose(wfd)
        self.rfds[subpid] = rfd
        return subpid

    def waitpid(self):
        subpid, status = waitpid(-1, WNOHANG)
        if subpid in self.rfds:
            osclose(self.rfds[subpid])
            del(self.rfds[subpid])
        return subpid, status

    def select(self, timeout):
        rfds, wfds, efds = select(self.rfds.values(), [], [], timeout)
        for rfd in rfds: self.wfwrite(self.readall(rfd))
        self.wfflush()

    def readall(self, rfd):
        body, body0 = '', osread(rfd, 1)
        while body0:
            body += body0
            body0 = osread(rfd, 1)
        return body

    def dolog(self, oper, message):
        if oper not in self.jdesc: return
        jdesc = self.jdesc[oper]
        lnfmt0 = jdesc.get('lnfmt0', self.jdesc['lnfmt0'])
        lnfmt1 = jdesc.get('lnfmt1', self.jdesc['lnfmt1'])
        kwargs = { 'idx': 0, 'oper': oper, 'pid': getpid() }
        nowobj = datetime.now()
        for idx in range(len(self.jdesc['tsfmts'])):
            kwargs['now%u' % idx] = nowobj.strftime(self.jdesc['tsfmts'][idx])
        for msgln in message.split('\n'):
            kwargs['msgln'] = msgln
            if kwargs['idx'] == 0: lnfmt = lnfmt0
            else: lnfmt = lnfmt1
            self.wfwrite(lnfmt % kwargs)
            kwargs['idx'] += 1
        self.wfflush()

    def exit(self):
        self.wfclose()
        sysexit()

    def warning(self, message): self.dolog('WARN', message)
    def error(self, message): self.dolog('ERR', message)
    def exception(self, message): self.dolog('EXC', message + format_exc())
    def progress(self, message): self.dolog('PROG', message)
    def database(self, message): self.dolog('DB', message)
    def storage(self, message): self.dolog('STOR', message)
    def source(self, message): self.dolog('SRC', message)
