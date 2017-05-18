import globals as g


class Graph:
    def __init__(self, maze):
        self.height = maze.height
        self.width = maze.width
        self.hubs = []
        self.edges = {}
        self.begin = None
        self.end = None
        self.vertex = self.__get_vertex(maze)
        self.__connect()

    def __get_vertex(self, maze):
        vertex = {}
        for i in range(0, maze.height):
            for j in range(0, maze.width):
                vertex[j, i] = self.__get_node(maze, (j, i))
        return vertex

    def __get_node(self, maze, pos):
        j, i = pos
        curr = maze.dots[j, i]
        up = maze.dots[j, i + 1] if (j, i + 1) in maze.dots else g.out
        down = maze.dots[j, i - 1] if (j, i - 1) in maze.dots else g.out
        left = maze.dots[j - 1, i] if (j - 1, i) in maze.dots else g.out
        right = maze.dots[j + 1, i] if (j + 1, i) in maze.dots else g.out

        directions = (up, down, left, right).count(g.free)

        if curr == g.free and (up == g.out or down == g.out or right == g.out or left == g.out):
            if self.begin is None:
                self.begin = (j, i)
                return g.hub
            elif self.end is None:
                self.end = (j, i)
                return g.hub

        if curr == g.wall:
            return g.wall
        if (up, down, left, right) == (g.free, g.free, g.wall, g.wall) or (up, down, left, right) == (
                g.wall, g.wall, g.free, g.free):
            return g.free
        if directions >= 2:
            return g.hub
        return g.free

    def __connect(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.vertex[j, i] == g.hub:
                    self.hubs.append((j, i))  # get list of hubs
                    self.edges[j, i] = []  # start edges as dictionary of lists

        for hub in self.hubs:
            x, y = hub
            if y < self.height - 1:
                j = y + 1
                while j < self.height - 1 and self.vertex[x, j] != g.wall and self.vertex[x, j] != g.hub:
                    j += 1
                if self.vertex[x, j] == g.hub:
                    self.edges[x, y].append((x, j))
                    self.edges[x, j].append((x, y))

            if x < self.width - 1:
                k = x + 1
                while k < self.width - 1 and self.vertex[k, y] != g.wall and self.vertex[k, y] != g.hub:
                    k += 1
                if self.vertex[k, y] == g.hub:
                    self.edges[x, y].append((k, y))
                    self.edges[k, y].append((x, y))

    def print_graph_nodes(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.vertex[j, i], end=' ')
            print()

    def print_graph_stats(self):
        print('Graph Nodes:')
        print(self.hubs)
        print('Graph Connections:')
        for hub in self.hubs:
            print(hub, '->', self.edges[hub])
