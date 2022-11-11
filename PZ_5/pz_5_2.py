import random

def SortDec3(A,B,C):
    L = []
    if A < B:
        A,B = B,A
    if B < C:
        B,C = C,B
    if A < B:
        A,B = B,A
    L.append(A)
    L.append(B)
    L.append(C)
    return L

A = random.randrange(-10,10)
B = random.randrange(-10,10)
C = random.randrange(-10,10)
print("Initial: {0}, {1}, {2}".format(A,B,C))
A,B,C = SortDec3(A,B,C)
print("Final: {0}, {1}, {2}".format(A,B,C))

A = random.randrange(-10,10)
B = random.randrange(-10,10)
C = random.randrange(-10,10)
print()
print("Initial: {0}, {1}, {2}".format(A,B,C))
A,B,C = SortDec3(A,B,C)
print("Final: {0}, {1}, {2}".format(A,B,C))
