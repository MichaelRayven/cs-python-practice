[n, m] = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input())
row = -1

for i in range(len(matrix)):
    current_max = 0
    count = 0
    prev = 0

    for j in range(len(matrix[0])):
        if prev == matrix[i][j]:
            count += 1
        else:
            count = 0

        if count > current_max:
            current_max = count

        prev = matrix[i][j]
    
    if (current_max + 1) >= k:
        row = i
        break

print(row + 1)

