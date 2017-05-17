from PIL import Image
from graph import Graph


class Maze:
    dots = {}
    height = 0
    width = 0
    solution = {}

    def __init__(self, image_path):
        image = Image.open(image_path)
        pixels = image.load()
        (self.width, self.height) = image.size
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.dots[j, i] = self.color(pixels[j, i])  # inverted i j to preserve image orientation

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
                print(self.dots[j, i], end=" ")
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
        directions = (up, down, left, right).count(' ')
        if directions >= 2:
            return hub
        return path

    def maze_to_graph(self):
        vertex = {}
        for i in range(0, self.height):
            for j in range(0, self.width):
                vertex[j, i] = self.get_node((j, i))

        graph = Graph(self.height, self.width, vertex)
        return graph

    def print_solution(self):
        path = '.'
        for i in range(0, len(self.solution)-1):
            x1, y1 = self.solution[i]
            x2, y2 = self.solution[i+1]
            if x1 == x2:
                if y1 > y2:
                    for j in range(y1, y2-1, -1):
                        self.dots[x1, j] = path
                else:
                    for j in range(y1, y2+1):
                        self.dots[x1, j] = path
            elif y1 == y2:
                if x1 > x2:
                    for j in range(x1, x2-1, -1):
                        self.dots[j, y1] = path
                else:
                    for j in range(x1, x2+1):
                        self.dots[j, y1] = path
        self.print()

    def solution_to_image(self, file_name):
        im = Image.new("RGB", (self.width, self.height))
        pix = im.load()
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.dots[j, i] == '#':
                    pix[j, i] = (0, 0, 0)
                elif self.dots[j, i] == ' ':
                    pix[j, i] = (255, 255, 255)
                else:
                    pix[j, i] = (255, 0, 0)

        im.save("images/"+file_name, "PNG")


