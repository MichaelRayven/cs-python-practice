[n, m] = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(list(input().split(maxsplit=m)[:-1]))


transposed_matrix = [row[:] for row in matrix]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transposed_matrix[j][i] = matrix[i][j]


for i in transposed_matrix:
    print(" ".join(i))