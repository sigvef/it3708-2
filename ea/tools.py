class Mixin(object):
    def __init__(self, fn):
        self.__call__ = fn

    def __call__(self, *args, **kwargs):
        return self.__call__(*args, **kwargs)
