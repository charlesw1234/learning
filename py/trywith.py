class ctx(object):
    def __enter__(self):
        print('__enter__', self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', self, exc_type, exc_value, traceback)
        return True

with ctx() as ctxobj:
    print('in with', ctxobj)
    raise RuntimeError('haha')
