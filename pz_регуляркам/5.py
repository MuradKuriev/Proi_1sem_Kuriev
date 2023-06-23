#Найдите слова, которые начинаются на гласную (\b — граница слова):

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344"
pattern = r'\b[АаЕеЁёИиОоУуЫыЭэЮюЯяAEIOUaeiou]\w*\b'

words_starting_with_vowel = re.findall(pattern, text)
print(words_starting_with_vowel)
