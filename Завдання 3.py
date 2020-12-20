import math

x = float(input("Введіть змінну х : "))
e = float(input("Введіть точність е: "))
S = 0
a = 1
while x ** (2 * a) / math.factorial(2 * a) > e:
    S = -1**a * x ** (2 * a) / math.factorial(2 * a)
    a += 1
print(S)
if math.cos(x) - S < e:
    print("справедлива")
else:
    print("несправедлива")