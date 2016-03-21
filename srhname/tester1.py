from sqlite3 import connect, OperationalError

conn = connect('bookinfo.db')
cursor = conn.cursor()
letters = 'abcdefghijklmnopqrstuvwxyz'

def doselect(table):
    names = []
    try: result = cursor.execute('SELECT title FROM %s;' % table)
    except OperationalError: return
    for row in result:
        name = row[0].strip()
        if name == u'': continue
        if name not in names: names.append(name)
    names.sort()
    for name in names:
        print(name.encode('utf8'))

for ch0 in letters:
    doselect('_' + ch0)
    for ch1 in letters:
        doselect('_' + ch0 + ch1)
