#Организовать словарь на 10 англо-русских слов, обеспечивающий
#"перевод" английского слова на русский.

def program():
  dic ={"Cat": "Кот",
        "House": "Дом",
        "Car": "Машина",
        "Hospital": "Больница",
        "Dog": "Собака",
        "Carrot": "Морковка",
        "A monkey": "Обезьяна",
        "Garden": "Огород",
        "Spider": "Паук",
        "Phone": "Телефон"}
  a = str(input())
  if a not in dic:
        print("Неверное значение")
        program()
  else:
        print(dic[a])
program()
