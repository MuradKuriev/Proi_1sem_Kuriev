#Найдите все натуральные числа (возможно, окружённые буквами):

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'\b\d+\b'

numbers = re.findall(pattern, text)
print(numbers)

