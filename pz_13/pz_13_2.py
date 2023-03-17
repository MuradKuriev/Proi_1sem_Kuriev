# Создаем матрицу
matrix = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]

# Выводим матрицу на экран
print("Матрица:")
for row in matrix:
    print(row)

# Ищем отрицательные элементы матрицы и формируем из них новый массив
negative_elements = []
for row in matrix:
    for elem in row:
        if elem < 0:
            negative_elements.append(elem)

# Выводим размер полученного массива на экран
print("Размер массива отрицательных элементов: {}".format(len(negative_elements)))
