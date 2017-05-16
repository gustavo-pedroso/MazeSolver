from queue import Queue


class BFSSolver:
    graph = None

    def __init__(self, graph):
        self.graph = graph

    def solve(self):
        final = self.graph.hubs[self.graph.n_hubs - 1]
        print('final = ',final)
        my_set = set()
        queue = Queue(maxsize=0)
        path = [self.graph.hubs[0]]

        my_set.add(self.graph.hubs[0])
        queue.put(self.graph.hubs[0])

        while queue.not_empty:
            v = queue.get()
            if v == final:
                break
            for k in self.graph.edges[v]:
                if k not in my_set:
                    my_set.add(k)
                    path.append(k)
                    queue.put(k)

        print(path)