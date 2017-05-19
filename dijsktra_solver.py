from solver import Solver
import math


class DijkstraSolver(Solver):
    @staticmethod
    def solve(graph):
        graph.get_distances()
        path = []
        distance = {}
        predecessor = {}
        my_set = set()

        for hub in graph.hubs:
            distance[hub] = math.inf
            my_set.add(hub)

        distance[graph.begin] = 0
        found = False

        while my_set:
            min_dist = math.inf
            for hub in distance.keys():
                if distance[hub] < min_dist:
                    closer = hub
                    min_dist = distance[hub]

            if closer in my_set:
                if closer == graph.end:
                    found = True
                    break
                my_set.remove(closer)
                del distance[closer]
            print(len(my_set))
            for con in graph.edges[closer]:
                if con in my_set:
                    alt = min_dist + graph.distances[closer, con]
                    if alt < distance[con]:
                        distance[con] = alt
                        predecessor[con] = closer

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


