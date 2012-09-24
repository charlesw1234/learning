#!/usr/bin/python
from json import loads as jsonloads
from json import dumps as jsondumps
from time import sleep
from urllib2 import urlopen, HTTPError

class stget(object):
    def __init__(self):
        self.urlfmt = 'http://www.weather.com.cn/data/sk/101%02u%02u%02u.html'
        self.data = []

    def get(self, lv0, lv1, lv2):
        url = self.urlfmt % (lv0, lv1, lv2)
        text = None
        while text is None:
            try:
                text = urlopen(url).read()
            except HTTPError, exc:
                print(exc)
                sleep(0.5)
        try:
            value = jsonloads(text)
        except ValueError:
            value = None
        print(url, value)
        return value

    def getall(self):
        lv0 = 1
        while lv0:
            arr0 = []
            lv1 = 1
            while lv1:
                jsk = self.get(lv0, lv1, 0)
                if jsk is not None: arr0.append(jsk)
                else:
                    arr1 = []
                    lv2 = 1
                    while True:
                        jsk = self.get(lv0, lv1, lv2)
                        if jsk is None: break
                        arr1.append(jsk)
                        lv2 = lv2 + 1
                    if arr1 != []: arr0.append(arr1)
                    else: break
                lv1 = lv1 + 1
            if arr0: self.data.append(arr0)
            else: break
            lv0 = lv0 + 1

stgetobj = stget()
stgetobj.getall()
open('dump.json', 'wt').write(jsondumps(stgetobj.data))
