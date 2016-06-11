from gzip import open as gzopen

class pinyin_library(object):
    def __init__(self, source):
        self.singles = u''
        self.pinyin_dict = {}
        self.frequency = {}
        for ln in gzopen(source, 'rt').readlines():
            body = ln.strip().split()
            thechr = unichr(int(body[0], base=16))
            if len(pinyins) == 1: self.singles += thechr
            self.frequency[thechr] = 0
            pinyins = map(lambda pinyin: pinyin.replace('u:', 'v'), body[1][1:-1].split(','))
            for pinyin in pinyins:
                if pinyin not in self.pinyin_dict: self.pinyin_dict[pinyin] = u''
                self.pinyin_dict[pinyin] += thechr

    def commit(self, text):
        for textchr in text:
            if textchr in self.frequency:
                self.frequency[textchr] += 1

    def pinyinchr(self, pinyin):
        pychr = None
        maxfrequency = 0
        for thechr in self.pinyin_dict[pinyin]:
            if thechr not in self.singles: continue
            if self.frequency[thechr] > maxfrequency:
                maxfrequency = self.frequency[thechr]
                pychr = thechr
        return pychr
