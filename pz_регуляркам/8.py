#Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки:

import re

text = "АААА аааа АаАаАаАа 123 123 12345 11223344\nQwertyЙцукен\n\n+-,/[](), *** (***), a*(b+[c+d])*e/f+g-h"
pattern = r'.*\(.*\).*'

lines_with_brackets = re.findall(pattern, text, re.MULTILINE)
print(lines_with_brackets)
