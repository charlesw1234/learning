from sqlite3 import connect, OperationalError

conn = connect('bookinfo.db')
cursor = conn.cursor()
letters = 'abcdefghijklmnopqrstuvwxyz'

def doselect(table):
    try: rows = cursor.execute('SELECT * FROM %s;' % table)
    except OperationalError: return
    for row in rows:
        row = (row[6], row[0], row[2], row[3])
        print(u','.join(row).encode('utf8'))

for ch0 in letters:
    doselect('_' + ch0)
    for ch1 in letters:
        doselect('_' + ch0 + ch1)
