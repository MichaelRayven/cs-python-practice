[height, width] = list(map(int, input().split()))

snake_char = "#"
empty_char = "."

for i in range(height):
    for j in range(width):
        if (i % 2 == 0 or 
            ((i // 2) % 2 == 0 and j == (width - 1)) or
            ((i // 2) % 2 == 1 and j == 0)
        ):
            print(snake_char, end="")
        else:
            print(empty_char, end="")
    print()