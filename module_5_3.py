# This is a Lesson module_5_2


class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name} Kол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            return print(f'Такого этажа не существует')
        for i in range(1, new_floor + 1):
            print(f'{i}')

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # (<)
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):  # (<=)
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):  # (>)
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # (>=)
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # (!=)
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return not (self.number_of_floors == other.number_of_floors)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        self = self + value
        return self

    def __radd__(self, value):
        self = self + value
        return self

    def __sub__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x - y
        return self

    def __mul__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x * y
        return self

    def __truediv__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x / y
        return self

    def __floordiv__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x // y
        return self

    def __mod__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x % y
        return self

    def __pow__(self, other):
        if isinstance(other.number_of_floors, int):
            x, y = self.number_of_floors, other.number_of_floors
            self.number_of_floors = x ** y
        return self


# It's a magik and overload


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

