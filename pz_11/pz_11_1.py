import random

# Генерируем случайную последовательность чисел
sequence = [random.randint(-100, 100) for _ in range(20)]

# Записываем последовательность в файл
with open('sequence.txt', 'w') as f:
    f.write('Исходные данные:\n')
    f.write(f'Количество элементов: {len(sequence)}\n')
    f.write(f'Максимальный элемент: {max(sequence)}\n')
    f.write(f'Среднее арифметическое элементов первой трети: {sum(sequence[:len(sequence)//3])/len(sequence)//3}\n')
    f.write('\n'.join(map(str, sequence)))
