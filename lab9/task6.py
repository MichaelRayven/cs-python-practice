n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(input().split(maxsplit=n)[:-1]))

new_matrix = [row[:] for row in matrix]
for i in range(n):
    new_matrix[i][i] = matrix[n - i - 1][i]
    new_matrix[n - i - 1][i] = matrix[i][i]

for i in new_matrix:
    print(" ".join(i))