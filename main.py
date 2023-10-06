class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.widht = width

    def perimeter(self):
        return 2 * (int(self.lenght) + int(self.widht))

    def area(self):
        return int(self.lenght) * int(self.widht)

    def display(self):
        print(self.lenght)
        print(self.widht)
        print(self.perimeter())
        print(self.area())


if __name__ == '__main__':

    rect = Rectangle('5', '2')
    rect.display()

