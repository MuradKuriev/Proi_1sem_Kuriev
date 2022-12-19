#Даны три целых числа: A, B , C. Проверить истинность высказывания
a = int(input())
b = int(input())
c = int(input())
if (a*b > 0) and (b*c > 0):
    print('верно')
else:
    print('неверно')
