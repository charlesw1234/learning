#!/usr/bin/python
from datetime import datetime

for year in range(1000, 3000):
    dt = datetime.strptime('%d-01-01' % year, '%Y-%m-%d')
    ydiff = year - 1600 - 1
    wday = (ydiff + ydiff / 4 - ydiff / 100 + ydiff / 400) % 7
    if wday != dt.weekday():
        print(year, dt.weekday(), wday, (dt.weekday() - wday + 7) % 7)
