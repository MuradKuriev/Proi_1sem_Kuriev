#Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами):

import re

text = '''
<a href="#10">10: CamelCase -> under_score</a>;
<a href="#11">11: Удаление повторов</a>;
<a href="#12">12: Близкие слова</a>;
<a href="#13">13: Форматирование больших чисел</a>;
<a href="#14">14: Разделить текст на предложения</a>;
<a href="#15">15: Форматирование номера телефона</a>;
<a href="#16">16: Поиск e-mail'ов — 2</a>;
'''

pattern = r'<a href="#\d+">.*?</a>'

table_of_contents = re.findall(pattern, text, re.DOTALL)
print(table_of_contents)
