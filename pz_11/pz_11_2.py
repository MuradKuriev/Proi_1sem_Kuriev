# Читаем содержимое файла
with open('text18-12.txt', 'r') as f:
    content = f.read()

# Выводим содержимое файла и количество пробельных символов
print(content)
print(f'Количество пробельных символов: {content.count(" ")}')

# Строим строку в стихотворной форме
poem = ''
for line in content.split('\n'):
    if not line:
        continue
    poem += f'{line},\n'
poem += '*' * 10

# Записываем стихотворение в файл
with open('poem.txt', 'w') as f:
    f.write(poem)
