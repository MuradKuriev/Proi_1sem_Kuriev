#Составить функцию, которая выполнит суммирования числового ряда.
def program(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = (list(map(int,(input('Введите ряд чисел:')).split())))
print(program(numbers))

