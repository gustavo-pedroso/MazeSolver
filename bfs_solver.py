from queue import Queue
from solver import Solver


class BFSSolver(Solver):

    @staticmethod
    def solve(graph):
        predecessor = {}
        path = []
        begin = graph.begin
        final = graph.end
        my_set = set()
        queue = Queue()

        my_set.add(begin)
        queue.put(begin)

        while queue.not_empty:
            v = queue.get()
            print(v)
            if v == final:
                found = True
                break
            for k in graph.edges[v]:
                if k not in my_set:
                    my_set.add(k)
                    predecessor[k] = v
                    queue.put(k)

        if not found:
            print('Solution not found!')
        i = predecessor[final]
        path.append(final)
        path.append(i)
        while i in predecessor:
            i = predecessor[i]
            path.append(i)
        return path
