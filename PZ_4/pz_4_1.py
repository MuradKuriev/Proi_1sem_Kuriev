

N = int(input())
print('N = ', N)

S = 0.0
for i in range(1,N+1):
    x = (1 + i*0.1)*(-1)**(i+1)
    S += x
    print(i," : ",x," : ",S)
print("Sum = ",S)