n = int(input("Введіть ціле значення n:"))
a = [0, 9, 9]
i = 3
while i <= n:
    el = a[i - 1] + 4 * (a[i - 3])
    a.append(el)
    i += 1

print("Весь список:{0}".format(a))
print("xn={0}".format(el))