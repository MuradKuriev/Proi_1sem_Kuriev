import random
N = int(input('Введите число'))
A = [random.randint(1,10) for i in range(N)]

print("N = ", N)
print(A)
j = N - 1
while j >=0 :
    print("{0} : {1}".format(j,A[j]))
    j -= 2
					
