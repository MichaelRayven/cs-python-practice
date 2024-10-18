string = input("Входная строка:")

for char in string:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        print(char, end="")