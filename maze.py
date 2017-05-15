from PIL import Image
from graph import Graph


class Maze:
    dots = {}
    height = 0
    width = 0

    def __init__(self, image_path):
        image = Image.open(image_path)
        pixels = image.load()
        (self.height, self.width) = image.size
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.dots[i, j] = self.color(pixels[j, i])  # inverted i j to preserve image orientation

    @staticmethod
    def color(pixel):
        a, b, c, d = pixel
        if a == 0:
            return '#'
        else:
            return ' '

    def print(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.dots[i, j], end=" ")
            print()

    def get_node(self, pos):
        i, j = pos

        path = '+'
        wall = '#'
        hub = '@'

        if (i+1, j) in self.dots:
            up = self.dots[i+1, j]
        else:
            up = '-'

        if (i-1, j) in self.dots:
            down = self.dots[i-1, j]
        else:
            down = '-'

        if (i, j-1) in self.dots:
            left = self.dots[i, j-1]
        else:
            left = '-'

        if (i, j+1) in self.dots:
            right = self.dots[i, j+1]
        else:
            right = '-'

        if self.dots[i, j] == '#':
            return wall
        if (up, down, left, right) == (' ', ' ', '#', '#'):
            return path
        if (up, down, left, right) == ('#', '#', ' ', ' '):
            return path
        return hub

    def maze_to_graph(self):
        vertex = {}
        for i in range(0, self.height):
            for j in range(0, self.width):
                vertex[i, j] = self.get_node((i, j))

        graph = Graph(self.height, self.width, vertex)
        return graph
