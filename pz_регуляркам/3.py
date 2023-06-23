# Найдите слова, в которых есть русская буква, а за ней цифра:

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'[А-Яа-я]+\s*\d+'

words_with_russian_letter_and_digit = re.findall(pattern, text)
print(words_with_russian_letter_and_digit)
