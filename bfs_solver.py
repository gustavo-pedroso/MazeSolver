from queue import Queue
from solver import Solver


class BFSSolver(Solver):

    @staticmethod
    def solve(graph):
        predecessor = {}
        path = []
        my_set = set()
        queue = Queue()

        my_set.add(graph.begin)
        queue.put(graph.begin)
        found = False

        while not queue.empty():
            v = queue.get_nowait()
            if v == graph.end:
                found = True
                break
            for k in graph.edges[v]:
                if k not in my_set:
                    my_set.add(k)
                    predecessor[k] = v
                    queue.put(k)

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
