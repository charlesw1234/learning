# -*- coding: utf-8 -*-
from sqlite3 import connect, OperationalError
from time import time
from nametree import Tree, Iterator

conn = connect('bookinfo.db')
cursor = conn.cursor()
letters = 'abcdefghijklmnopqrstuvwxyz'

def doselect(treeobj, table):
    names = []
    try: result = cursor.execute('SELECT title FROM %s;' % table)
    except OperationalError: return
    for row in result:
        name = row[0].strip()
        if name == u'': continue
        if name not in names: names.append(name)
    names.sort()
    treeobj.commit(names)

treeobj = Tree()
for ch0 in letters:
    doselect(treeobj, '_' + ch0)
    for ch1 in letters:
        doselect(treeobj, '_' + ch0 + ch1)
treeobj.finish()

wfp = open('bookinfo.bin', 'wb')
map(lambda piece: wfp.write(piece), treeobj.dump())
wfp.close()

minsz = maxsz = 0
for idx in range(len(treeobj.tree)):
    node = treeobj.tree[idx]
    #print(idx, node)
    if node[2] < minsz: minsz = node[2]
    if node[2] > maxsz: maxsz = node[2]
#print(repr(treeobj.tails))

#print('--------------')
#print(len(treeobj.tree), len(treeobj.tails), minsz, maxsz)

tv0 = time()
iterator = Iterator(treeobj)
print(iterator.get().encode('utf-8'))
while iterator.donext():
    print(iterator.get().encode('utf-8'))
tv1 = time()
print(tv1 - tv0)
