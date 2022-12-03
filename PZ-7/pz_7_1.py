s = input('Введите строку: ')
n = int(input('Введите число: '))
for i in range(len(s)):
  print(s[i], "*"*n, sep='', end="")
