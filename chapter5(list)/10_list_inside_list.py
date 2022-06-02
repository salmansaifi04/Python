# list inside list
matrix = [[1,2,3],[4,5,6],[7,8,9]]  # 2d list

print(matrix[0])
print(matrix[1])
print(matrix[2])

# loop in list
for i in matrix:
    for j in i:
        print(j)

print(matrix[0][1])