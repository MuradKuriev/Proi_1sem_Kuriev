#Дано целое число. Вывести его строку-описание вида «отрицательное четное
#число», «нулевое число», «положительное нечетное число» и т. д.
i=int(input())
if i == 0:
    s = "нулевое "
elif i > 0:
    s = "положительное "
else:
    s = "отрицательное "
if i != 0:
    if i % 2 == 0:
        s += "четное "
    else:
        s += "нечетное "
s += "число"
print(i, " : ", s)
