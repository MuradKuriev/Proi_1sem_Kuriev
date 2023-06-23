#Найдите пустые строчки:

import re

text = '''
АААА аааа АаАаАаАа 123 123 12345 11223344

QwertyЙцукен


+-,/[](), *** (***), a*(b+[c+d])*e/f+g-h
'''

pattern = r'^\s*$'

empty_lines = re.findall(pattern, text, re.MULTILINE)
print(empty_lines)
