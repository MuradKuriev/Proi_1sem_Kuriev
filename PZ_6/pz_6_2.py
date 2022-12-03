list1 = (list(map(int, (input('Введите ряд чисел: ')).split())))
sum = 0
for i in range(len(list1)-1):
  if (list1[i] + list1[i+1] > sum):
    sum = list1[i] + list1[i+1]
    a = i
print(f'Сумма {a+1} и {a+2} элементов равна: {sum}')
