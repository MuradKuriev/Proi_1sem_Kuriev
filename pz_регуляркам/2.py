#Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв):

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'\b[A-Я]+\b'

uppercase_words = re.findall(pattern, text)
print(uppercase_words)

