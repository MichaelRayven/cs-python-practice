import os

dir = os.path.dirname(__file__)



with open(os.path.join(dir, "file4.txt"), "r", encoding="utf8") as file:
    [winner_name, winner_surname, max_score] = file.readline().split()
    for line in file.readlines():
        [name, surname, score] = line.split()
        if int(score) > int(max_score):
            [winner_name, winner_surname, max_score] = line.split()

with open(os.path.join(dir, "file4.txt"), "r", encoding="utf8") as file:
    [prizewinner_name, prizewinner_surname, prizewinner_max_score] = file.readline().split()
    for line in file.readlines():
        [name, surname, score] = line.split()
        if int(score) > int(prizewinner_max_score) and int(score) < int(max_score):
            [prizewinner_name, prizewinner_surname, prizewinner_max_score] = line.split()

print(prizewinner_name, prizewinner_surname, f"Набранное количество баллов: {prizewinner_max_score}")