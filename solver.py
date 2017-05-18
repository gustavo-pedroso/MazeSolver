from abc import ABCMeta, abstractmethod


class Solver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def solve(self, graph): pass
