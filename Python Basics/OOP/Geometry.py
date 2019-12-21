class Circle:
    coefficient = 3.14159

    def __init__(self, size):
        self.size = size

    def area(self):
        return self.coefficient * pow(self.size, 2)

    def perimeter(self):
        return 2 * self.coefficient * self.size

    def scale(self, n):
        self.size *= n

    def __str__(self):
        return 'Circle'.center(30, '-') + \
               f'\n\tRadius:\t\t{self.size}\n\tPerimeter:\t{self.perimeter():.2f}\n\tArea:\t\t{self.area():.2f}'


class Square(Circle):
    coefficient = 4

    def __str__(self):
        return 'Square'.center(30, '-') + \
               f"\n\tSide:\t\t{self.size}\n\tPerimeter:\t{self.perimeter():.2f}\n\tArea:\t\t{self.area():.2f}"


c = Circle(5)
s = Square(5)
c.scale(2)
print(c)
print(s)
