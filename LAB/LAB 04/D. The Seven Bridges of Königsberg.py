def checkEulerianPath(vertex_count, edge_count, start, end):
    if len(start) != edge_count or len(end) != edge_count:
        return "NO"

    degree = [0] * (vertex_count + 1)
    for i in range(edge_count):
        degree[start[i]] += 1
        degree[end[i]] += 1

    odd_count = 0
    for i in range(1, vertex_count+1):
        if degree[i]%2 == 1:
            odd_count += 1

    if odd_count == 0 or odd_count == 2:
        return "YES"
    return "NO"


# Handling inputs:
first_input = input().split(" ")
vertex_count, edge_count = int(first_input[0]), int(first_input[1])

if edge_count == 0:
    print("YES")
else:
    start = input().split()
    end = input().split()

    # Turning my nodes into integers
    for i in range(len(start)):
        start[i] = int(start[i])
        end[i] = int(end[i])

    print(checkEulerianPath(vertex_count, edge_count, start, end))
