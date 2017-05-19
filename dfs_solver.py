from queue import LifoQueue
from solver import Solver


class DFSSolver(Solver):

    @staticmethod
    def solve(graph):
        path = []
        predecessor = {}
        my_set = set()
        stack = LifoQueue()

        stack.put(graph.begin)

        found = False

        while not stack.empty():
            v = stack.get()
            if v == graph.end:
                found = True
                break
            if v not in my_set:
                my_set.add(v)
                for k in graph.edges[v]:
                    if k not in my_set:
                        predecessor[k] = v
                        stack.put(k)

        if not found:
            print('No Solution Found!')
            return None

        i = predecessor[graph.end]
        path.append(graph.end)
        path.append(i)
        while i in predecessor:
            i = predecessor[i]
            path.append(i)
        return path
