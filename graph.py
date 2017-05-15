class Graph:
    height = 0
    width = 0
    vertex = {}
    edges = {}

    def __init__(self, height, width, vertex):
        self.height = height
        self.width = width
        self.vertex = vertex

    def print(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.vertex[i, j], end=' ')
            print()
