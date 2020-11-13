import random
matrix_table = []
for i in range(100, 590, 20):
    for j in range(100, 590, 20):
        matrix_table.append((i, j))

for i in matrix_table:
    print(i)
new_apple = random.randint(1, len(matrix_table))
print(new_apple)
print(matrix_table[new_apple])
print(matrix_table[new_apple][0])
print(matrix_table[new_apple][1])
print(type(matrix_table))
print(type(matrix_table[new_apple]))