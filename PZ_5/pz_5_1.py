numbers = (list(map(int,(input('Введите ряд чисел:')).split())))
total = 0
for number in numbers:
    total += number
print(total)
