class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Car(Transport):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)
        self.body_type = body_type

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Body Type:", self.body_type)

# Пример использования
car1 = Car("Toyota", "Camry", 2020, "Sedan")
car1.display_info()

car2 = Car("Tesla", "Model S", 2022, "Electric Sedan")
car2.display_info()
