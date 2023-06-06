import re

# Открываем исходный файл для чтения
with open('dates.txt', 'r') as file:
    text = file.read()

# Ищем все даты в формате ДД.ММ.ГГГГ
dates_dd_mm_yyyy = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

# Ищем все даты в формате ДД/ММ/ГГГГ
dates_dd_mm_yyyy_slash = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

# Подсчитываем количество дат в каждом формате
count_dd_mm_yyyy = len(dates_dd_mm_yyyy)
count_dd_mm_yyyy_slash = len(dates_dd_mm_yyyy_slash)

# Выводим результаты
print("Количество дат в формате ДД.ММ.ГГГГ:", count_dd_mm_yyyy)
print("Количество дат в формате ДД/ММ/ГГГГ:", count_dd_mm_yyyy_slash)

# Открываем новый файл для записи дат февраля в формате ДД/ММ/ГГГГ
with open('february_dates.txt', 'w') as file:
    # Ищем все даты февраля в формате ДД/ММ/ГГГГ
    february_dates = re.findall(r'\b\d{2}/02/\d{4}\b', text)
    # Записываем найденные даты в файл
    for date in february_dates:
        file.write(date + '\n')

print("Даты февраля в формате ДД/ММ/ГГГГ сохранены в файле 'february_dates.txt'")
