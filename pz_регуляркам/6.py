#Найдите все натуральные числа, не находящиеся на границе слова:

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'\b\d+\b'

numbers_not_at_word_boundary = re.findall(pattern, text)
print(numbers_not_at_word_boundary)
