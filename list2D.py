

numbers = [5, 2, 1, 7, 4]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



numbers.append(5)
print(numbers.count(5))





matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
        