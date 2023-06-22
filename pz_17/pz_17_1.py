class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print("Имя:", self.name)
        print("Вид:", self.species)


# Пример использования класса "Животное"
animal1 = Animal("Лев", "хищник")
animal1.display_info()

animal2 = Animal("Заяц", "травоядное")
animal2.display_info()
