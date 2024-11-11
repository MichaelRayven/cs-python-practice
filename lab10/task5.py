import os

dir = os.path.dirname(__file__)


user_content = input()

FILE_NAME = "my_file.txt"
file_path = os.path.join(dir, FILE_NAME)

if os.path.exists(file_path):
    lines = []
    with open(file_path, "r", encoding="utf8") as file:
        lines = file.readlines()
        print(lines)
    with open(file_path, "w", encoding="utf8") as file:
        middle = len(lines) // 2
        lines.insert(middle, user_content + "\n")
        file.write("".join(lines))
else:
    with open(file_path, "w", encoding="utf8") as file:
        file.write(user_content)