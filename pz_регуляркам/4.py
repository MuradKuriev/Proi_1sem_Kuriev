#Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова):


import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'\b[А-ЯA-Z]\w*\b'

words_starting_with_uppercase = re.findall(pattern, text)
print(words_starting_with_uppercase)
