import sys
sys.setrecursionlimit(200000)

N=int(input())

graph={}
for i in range(1, N+1):
    graph[i]=[]

for i in range(N-1):
    uv=input().split(" ")
    u=int(uv[0])
    v=int(uv[1])
    graph[u].append(v)
    graph[v].append(u)

def DFS(current, parent, distance, graph):
    last_node=current
    max_distance=distance
    for i in graph[current]:
        if i!=parent:
            node, dist=DFS(i, current, distance+1, graph)
            if dist>max_distance:
                max_distance=dist
                last_node=node
    return last_node, max_distance

first_endpoint, last_endpoint=DFS(1, -1, 0, graph)
second_endpoint, longest_distance=DFS(first_endpoint, -1, 0, graph)

print(longest_distance)
print(first_endpoint, second_endpoint)