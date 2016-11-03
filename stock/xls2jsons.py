import xlrd
from json import dumps as jdumps

docobj = xlrd.open_workbook('20161102.xlsx')
table = docobj.sheet_by_index(0)
for rowidx in range(table.nrows):
    row = table.row_values(rowidx)
    print(jdumps(row, ensure_ascii = False).encode('utf8'))
