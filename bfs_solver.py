from queue import Queue


class BFSSolver:
    graph = None

    def __init__(self, graph):
        self.graph = graph

    def solve(self):
        pred = {}
        path = []
        begin = self.graph.begin
        final = self.graph.end
        my_set = set()
        queue = Queue(maxsize=0)

        my_set.add(begin)
        queue.put(begin)

        while queue.not_empty:
            v = queue.get()
            if v == final:
                break
            for k in self.graph.edges[v]:
                if k not in my_set:
                    my_set.add(k)
                    pred[k] = v
                    queue.put(k)

        i = pred[final]
        x, y = final
        path.append((x, y+1))
        path.append(final)
        path.append(i)
        while i in pred:
            if i in pred:
                i = pred[i]
                path.append(i)
        x, y = begin
        path.append((x, y-1))
        return path
