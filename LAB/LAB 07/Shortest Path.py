import heapq

vertex, edge, source, destination=map(int, input().split( ))
src=list(map(int, input().split( )))
dst=list(map(int, input().split( )))
weights=list(map(int, input().split( )))

adj_list={}
for i in range(1, vertex+1):
    adj_list[i]=[]

for i in range(edge):
    adj_list[src[i]].append((dst[i], weights[i]))

distances={}
parent={}
for i in range(1, vertex+1):
    distances[i]=float("inf")
    parent[i]=None

distances[source]=0

heap=[(0, source)]

while heap:
    current_distance, current_node=heapq.heappop(heap)
    if current_distance>distances[current_node]:
        continue
    for neighbor, weight in adj_list[current_node]:
        new_distance=current_distance+weight
        if new_distance<distances[neighbor]:
            distances[neighbor]=new_distance
            parent[neighbor]=current_node
            heapq.heappush(heap, (new_distance,neighbor))

if distances[destination]==float("inf"):
    print(-1)
else:
    print(distances[destination])
    path=[]
    pointer=destination
    for i in range(vertex):
        if pointer==None:
            break
        path.append(pointer)
        pointer=parent[pointer]
    for node in path[::-1]:
        print(node, end=" ")