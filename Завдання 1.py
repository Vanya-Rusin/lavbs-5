n = int(input("введіть значення n:"))
S = 0
while n >= 1:
    S += (2*n)**2+(2*n+1)**3
    n -= 1
print(S)