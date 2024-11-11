import os

dir = os.path.dirname(__file__)



with open(os.path.join(dir, "file5.txt"), "r", encoding="utf8") as file:
    index = file.read().find("Academy")
    if index != -1:
        print(f"In file5.txt at character number {index + 1}")
    else:
        print("file6.txt")