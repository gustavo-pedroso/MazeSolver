from PIL import Image
import globals as g


class Maze:
    def __init__(self, image_path):
        self.dots = {}
        self.solution = {}
        image = Image.open(image_path)
        image = image.convert('RGB')
        pixels = image.load()
        (self.width, self.height) = image.size
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.dots[j, i] = self.__color(pixels[j, i])  # inverted i j to preserve image orientation

    @staticmethod
    def __color(pixel):
        return g.wall if pixel == g.black else g.free

    def print(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.dots[j, i], end=' ')
            print()

    def print_solution(self):
        if self.solution is not None:
            for i in range(0, len(self.solution)-1):
                x1, y1 = self.solution[i]
                x2, y2 = self.solution[i+1]
                if x1 == x2:
                    if y1 > y2:
                        for j in range(y1, y2-1, -1):
                            self.dots[x1, j] = g.path
                    else:
                        for j in range(y1, y2+1):
                            self.dots[x1, j] = g.path
                elif y1 == y2:
                    if x1 > x2:
                        for j in range(x1, x2-1, -1):
                            self.dots[j, y1] = g.path
                    else:
                        for j in range(x1, x2+1):
                            self.dots[j, y1] = g.path
            self.print()

    def solution_to_image(self, file_name):
        if self.solution is not None:
            image = Image.new('RGB', (self.width, self.height))
            pix = image.load()
            for i in range(0, self.height):
                for j in range(0, self.width):
                    if self.dots[j, i] == g.wall:
                        pix[j, i] = g.black
                    elif self.dots[j, i] == g.free:
                        pix[j, i] = g.white
                    else:
                        pix[j, i] = g.red
            image.save('images/'+file_name, 'PNG')
