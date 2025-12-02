# I used the Euclidean Method to deduce the Greatest Common Divisor (GCD).
def gcd(i, j):
    while j != 0:
        i, j = j, i % j
    return i


def coprimeGraph(X, K):
    if K <= len(neighbors[X]):
        return neighbors[X][K-1]
    else:
        return -1


# Handling inputs:
vertices, queries = map(int, input().split())

neighbors = []
for i in range(vertices + 1):
    neighbors.append([])

for i in range(1, vertices + 1):
    for j in range(1, vertices + 1):
        if i != j and gcd(i, j) == 1:
            neighbors[i].append(j)
    neighbors[i].sort()

for _ in range(queries):
    X, K = map(int, input().split())
    print(coprimeGraph(X, K))
