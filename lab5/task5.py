a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

print("Этот треугольник...")
if (a == b and b == c):
    print("Равносторонний")
elif (a == b or b == c or c == a):
    print("Равнобедренный")
else:
    print("Разносторонний")