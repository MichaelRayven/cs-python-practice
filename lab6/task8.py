binary_num = input("Введите число в двоичной системе исчисления: ")
decimal_num = 0
exponent = 0

for i in range(len(binary_num) - 1, -1, -1):
    decimal_num += int(binary_num[i])*2**exponent
    exponent += 1

print(decimal_num)