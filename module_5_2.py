# This is a Lesson module_5_2

class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            return print(f'Такого этажа не существует')
        for i in range(1, new_floor + 1):
            print(f'{i}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:, {self.name}, кол-во этажей:, {self.number_of_floors}'


# h1 = House('ЖК Горский', 18)
# 2 = House('Домик в деревне', 2)

# h1.go_to(5)
# h2.go_to(10)

# It's a magik __str__ and __Len__
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
