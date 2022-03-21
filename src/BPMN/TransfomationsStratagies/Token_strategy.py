import abc

class _TokenStrategy():

    @abc.abstractclassmethod
    def transform(*args, **kwargs):
        pass