
max_height = -1
min_height = 99999999
count = 0
height = -1

while height != 0:
    height = int(input(f"Введите рост: "))
    if height > 0:
        count += 1
        
        if height > max_height:
            max_height = height
        
        if height < min_height:
            min_height = height

if count < 2:
    print(f"""Самый высокий человек с ростом: {max_height}
Самый низкий человек с ростом: {min_height}""")
else:
    print(f"Некого сравнивать")
