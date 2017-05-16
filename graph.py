class Graph:
    height = 0
    width = 0
    vertex = {}
    hubs = {}
    edges = {}
    n_hubs = 0

    def __init__(self, height, width, vertex):
        self.height = height
        self.width = width
        self.vertex = vertex

    def print(self):
        for i in range(0, self.height):
            print(i, end=' ')
            for j in range(0, self.width):
                print(self.vertex[i, j], end=' ')
            print()

    def connect(self):
        hub_num = 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.edges[i, j] = []
                if self.vertex[i, j] == '@':
                    self.hubs[hub_num] = (i, j)
                    hub_num += 1
        self.n_hubs = hub_num
        for i in range(0, hub_num):
            x, y = self.hubs[i]

            if y < self.height-1:
                j = y+1
                while j < self.height-1 and self.vertex[x, j] != '#' and self.vertex[x, j] != '@':
                    j += 1
                if self.vertex[x, j] == '@':
                    self.edges[x, y].append((x, j))
                    self.edges[x, j].append((x, y))

            if x < self.width-1:
                k = x + 1
                while k < self.width-1 and self.vertex[k, y] != '#' and self.vertex[k, y] != '@':
                    k += 1
                if self.vertex[k, y] == '@':
                    self.edges[x, y].append((k, y))
                    self.edges[k, y].append((x, y))

    def print_conn(self):
        for hub in self.hubs.values():
            print(hub, '->', self.edges[hub])






