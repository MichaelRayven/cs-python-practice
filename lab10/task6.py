import os

dir = os.path.dirname(__file__)

file_name = input()
file_path = os.path.join(dir, file_name)
reversed_file_path = os.path.join(dir, "reversed " + file_name)

with open(file_path, "r", encoding="UTF-8") as file:
    with open(reversed_file_path, "w", encoding="UTF-8") as reversed_file:
        for line in file.readlines():
            for word in line.split():
                print(word[::-1], end=" ")
                reversed_file.write(word[::-1] + " ")
            print()
            reversed_file.write("\n")