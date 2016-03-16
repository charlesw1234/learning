class Tree(object):
    def __init__(self):
        self.tree = []
        self.tails = u''
        self.top = []

    def commit(self, names):
        names.sort()
        result = self.dobranch(u'', names)
        if isinstance(result, list): self.top.extend(result)
        else: raise RuntimeError, repr(result)

    def finish(self):
        node = (u'', len(self.tree), len(self.top))
        self.tree.extend(self.top)
        self.tree.append(node)
        del(self.top)

    def dobranch(self, prefix, names):
        if len(names) == 1: return self.dobranch1(prefix, names[0])
        return self.dobranchn(prefix, names)

    def dobranch1(self, prefix, name):
        if prefix != u'': return self.dotail(prefix, name)
        branch = self.dotail(name[0], name[1:])
        result = [(name[0], len(self.tree), len(branch))]
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
                if subnames: branch.extend(self.dobranch(prefix + curch, subnames))
                curch = name[0]
                subnames = [name[1:]]
        if subnames: branch.extend(self.dobranch(prefix + curch, subnames))
        if prefix == u'': return branch
        result = [(prefix[-1], len(self.tree), len(branch))]
        self.tree.extend(branch)
        return result

    def dotail(self, prefix, name):
        start = self.tails.find(name)
        if start < 0:
            start = len(self.tails)
            self.tails = self.tails + name
        return [(prefix[-1], start, -len(name))]

class Iterator(object):
    def __init__(self, treeobj):
        self.treeobj = treeobj
        self.prefix = u''
        idx = len(self.treeobj.tree) - 1
        self.stack = [idx]
        self.prefix = self.prefix + self.treeobj.tree[idx][0]
        while self.treeobj.tree[idx][2] > 0:
            idx = self.treeobj.tree[idx][1]
            self.stack.append(idx)
            self.prefix = self.prefix + self.treeobj.tree[idx][0]

    def get(self):
        node = self.treeobj.tree[self.stack[-1]]
        if node[2] == 0: return self.prefix
        return self.prefix + self.treeobj.tails[node[1]: node[1] - node[2]]

    def donext(self):
        # pop phase.
        while True:
            self.stack[-1] = self.stack[-1] + 1
            if self.stack[-1] >= len(self.treeobj.tree): return False
            node = self.treeobj.tree[self.stack[-2]]
            if node[2] < 1: raise RuntimeError
            if self.stack[-1] < node[1] + node[2]: break
            self.stack.pop(-1)
            self.prefix = self.prefix[:-1]
        # push phase.
        node = self.treeobj.tree[self.stack[-1]]
        self.prefix = self.prefix[:-1] + node[0]
        while node[2] > 0:
            idx = node[1]
            self.stack.append(idx)
            node = self.treeobj.tree[idx]
            self.prefix = self.prefix + node[0]
        return True
