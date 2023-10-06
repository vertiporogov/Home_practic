from datetime import date
class Rectangle:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__widht = width

    def perimeter(self):
        return 2 * (int(self.__lenght) + int(self.__widht))

    def area(self):
        return int(self.__lenght) * int(self.__widht)

    def display(self):
        print(self.__lenght)
        print(self.__widht)
        print(self.perimeter())
        print(self.area())


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f'{self.__name}. {self.__age}')

    @classmethod
    def fromBirthYear(cls, name, year):
        age = date.today().year - int(year)
        return cls(name, age)




if __name__ == '__main__':

    # rect = Rectangle('5', '2')
    # rect.display()
    person = Person('Иван', 19)
    person.display()

    person1 = Person.fromBirthYear('Николай', 2000)
    person1.display()


