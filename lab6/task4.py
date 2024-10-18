n = int(input("Введите высоту елочки: "))

for i in range(n):
    print(" "*(n - i - 1), "#"*(1 + 2*i), sep="")

print(" "*(n-1), "#", sep="")