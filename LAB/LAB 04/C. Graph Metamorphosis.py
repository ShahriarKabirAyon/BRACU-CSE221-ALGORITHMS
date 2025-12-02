# Building a matrix
vertex_count = int(input())
matrix = []
for _ in range(vertex_count):
    row = [0] * vertex_count
    matrix.append(row)

for node in range(vertex_count):
    arr = input().split(" ")
    number_of_adjacent_nodes = int(arr[0])
    arr = arr[1::]
    
    # Turning it all into a bunch of integers
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    # arr = [1, 2]
    for j in range(number_of_adjacent_nodes):
        matrix[node][arr[j]] = 1

# Aligning my print statement according to Codeforces I/O format:
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
