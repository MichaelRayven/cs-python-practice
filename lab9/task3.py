treasure_count = int(input("Количество сокровищ:\n"))
treasure_coordinates_list = []


print("Координаты сокровищ:\n")
for i in range(treasure_count):
    treasure_coordinates = list(map(int, input().split()))
    treasure_coordinates_list.append(treasure_coordinates)

print("Координаты Александра:\n")
person_coordinates = list(map(int, input().split()))

closest = None
closest_sqr_distance = 9999999 # Arbitrary large number
for i in range(treasure_count):
    x_difference = person_coordinates[0] - treasure_coordinates_list[i][0]
    y_difference = person_coordinates[1] - treasure_coordinates_list[i][1]
    sqr_distance = x_difference**2 + y_difference**2

    if sqr_distance < closest_sqr_distance:
        closest = treasure_coordinates[i]
    
print(" ".join(closest))
