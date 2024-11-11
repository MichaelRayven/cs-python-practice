import os

dir = os.path.dirname(__file__)


user_content = input()
with open(os.path.join(dir, "my_file.txt"), "w", encoding="utf8") as file:
    lines = file.readlines()
    middle = len(lines) // 2
    
    if len(lines) > 2:
        file.write("\n".join(lines[0:middle]))
        file.write("\n" + user_content)
        file.write("\n" + "\n".join(lines[middle:]))
    else:
        file.write("\n".join(lines))
        file.write("\n" + user_content)