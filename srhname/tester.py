from nametree import Tree, Iterator

treeobj = Tree()

treeobj.commit(['aaxyz', 'aaaxyz', 'aaaadef', 'aabdef', 'aacdef', 'def'])
treeobj.finish()
wfp = open('bookinfo.bin', 'wb')
map(lambda piece: wfp.write(piece), treeobj.dump())
wfp.close()

for idx in range(len(treeobj.tree)):
    print(idx, treeobj.tree[idx])
print(repr(treeobj.tails))

iterator = Iterator(treeobj)

idx = 0
print(idx, iterator.get())
while iterator.donext():
    idx = idx + 1
    print(idx, iterator.get())
