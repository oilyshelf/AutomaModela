import abc


class BPMNComponent:

    @abc.abstractclassmethod
    def execute(*args, **kwargs):
        pass
