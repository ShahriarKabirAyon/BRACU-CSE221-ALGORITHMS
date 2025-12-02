vertex_count, edge_count = map(int, input().split())
source = list(map(int, input().split()))       # [2, 5, 4, 3, 2, 4, 3, 4, 1, 3]
destination = list(map(int, input().split()))  # [5, 1, 5, 5, 1, 2, 2, 1, 3, 4]

# Code in the following multi-line comment was used to visualise the matrix.
"""
matrix = []
for _ in range(vertex_count):
    row = [0] * vertex_count
    matrix.append(row)

i = 0
while i < len(source):
    matrix[source[i]-1][destination[i]-1] = 1
    i += 1
print("\n\n")
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()
"""
difference = {}
for i in range(1, vertex_count+1):
    difference[i] = 0

for src in source:
    difference[src] -= 1

for dest in destination:
    difference[dest] += 1

for value in difference.values():
    print(value, end=" ")
