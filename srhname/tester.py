from maker import TreeMaker

tmobj = TreeMaker()

tmobj.commit(['aaxyz', 'aaaxyz', 'aaaadef', 'aabdef', 'aacdef', 'def'])

for idx in range(len(tmobj.tree)):
    print(idx, tmobj.tree[idx])
print(repr(tmobj.tails))
print(tmobj.top)
