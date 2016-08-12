# -*- coding: utf-8 -*-
from datetime import datetime
from json import loads as jloads

class StockOperation(object):
    def __init__(self, row):
        self.date = datetime.strptime(row[0], '%Y%m%d')
        self.code = row[1]
        self.name = row[2]
        self.price = row[3]
        self.quantity = row[4]
        self.operation = row[5]
        self.amount = row[6]
        self.remain = row[7]
        
class StockOperations(list):
    def __init__(self):
        super(StockOperations, self).__init__()

    def summary(self):
        firstdate, lastdate = self[0].date, self[-1].date
        sum_quantity, sum_amount = 0, 0
        for soobj in self:
            sum_amount += soobj.amount
            if soobj.operation not in [u'股息入账']: sum_quantity += soobj.quantity
            if soobj.operation in [u'余额入账', u'转托转入']:
                sum_amount -= soobj.price * soobj.quantity
        return firstdate, lastdate, sum_quantity, sum_amount

stockdict = {}
for jrow in open('stock.flow.jsons', 'rt').readlines():
    row = jloads(jrow.strip())
    if row[1] == u'证券代码': continue
    if not row[1]: continue
    if row[1] not in stockdict: stockdict[row[1]] = StockOperations()
    stockdict[row[1]].append(StockOperation(row))

def soscmp(sosobj0, sosobj1): return cmp(sosobj0[-1].date, sosobj1[-1].date)

sosobjs = stockdict.values()
sosobjs.sort(cmp = soscmp)
for sosobj in sosobjs:
    summary = sosobj.summary()
    if summary[2] == 0: cost = 0
    else: cost = - summary[3] / summary[2]
    desc = '%s(%s): [%u/%u: %s~%s], %d, %.2f, %.2f' %\
           (sosobj[0].name, sosobj[0].code, (summary[1] - summary[0]).days, len(sosobj),
            summary[0].strftime('%Y%m%d'), summary[1].strftime('%Y%m%d'),
            summary[2], summary[3], cost)
    print(desc.encode('utf-8'))
