class dotdict(dict):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        return self.__setitem__(name, value)

ddobj = dotdict(yes = 1, no = 0)
print(ddobj.yes, ddobj.no)
ddobj.yes = 2
print(repr(ddobj))
