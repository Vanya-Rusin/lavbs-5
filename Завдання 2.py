n = int(input("Введіть ціле число: "))
m = 0

while n > 0:
    s = n % 10
    n = n // 10
    m = m * 10
    m = m + s

print('m =', m)