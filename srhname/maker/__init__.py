class TreeMaker(object):
    def __init__(self):
        self.tree = []
        self.tails = u''
        self.top = []

    def commit(self, names):
        names.sort()
        self.top.extend(self.dobranch(u'', names))

    def dobranch(self, prefix, names):
        if len(names) == 1: return self.dobranch1(prefix, names[0])
        return self.dobranchn(prefix, names)

    def dobranch1(self, prefix, name):
        if prefix != u'': return self.dotail(prefix, name)
        branch = [self.dotail(name[0], name[1:])]
        result = (name[0], len(self.tree), len(branch))
        self.tree.extend(branch)
        return result

    def dobranchn(self, prefix, names):
        branch = []
        curch = None
        subnames = []
        for name in names:
            if name == u'': branch.append((u'', 0, 0))
            elif name[0] == curch: subnames.append(name[1:])
            else:
                if subnames: branch.append(self.dobranch(prefix + curch, subnames))
                curch = name[0]
                subnames = [name[1:]]
        if subnames: branch.append(self.dobranch(prefix + curch, subnames))
        if prefix == u'': return branch
        result = (prefix[-1], len(self.tree), len(branch))
        self.tree.extend(branch)
        return result

    def dotail(self, prefix, name):
        start = self.tails.find(name)
        if start < 0:
            start = len(self.tails)
            self.tails = self.tails + name
        return (prefix[-1], start, -len(name))
