#Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными
#номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не
#использовать
import random
N = int(input('Введите число'))
A = [random.randint(1,10) for i in range(N)]

print("N = ", N)
print(A)
j = N - 1
while j >=0 :
    print("{0} : {1}".format(j,A[j]))
    j -= 2
					
