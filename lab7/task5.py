import re

sentence = input("Введите предложение: ")
lines = re.split(r"[/\n]\s*", sentence)
for i in range(len(lines)):
    print(lines[i])