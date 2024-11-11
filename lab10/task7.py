from random import choice
import os

dir = os.path.dirname(__file__)

file_path = os.path.join(dir, "words.txt")


words = []
with open(file_path, "r", encoding="UTF-8") as file:
    for line in file.readlines():
        word = line.strip().capitalize()
        if len(word) >= 3 and len(word) <= 7:
            words.append(word)
        
first_word = choice(words)
second_word = choice(words)
while len(first_word + second_word) < 8 or len(first_word + second_word) > 10:
    second_word = choice(words)

print(first_word + second_word)