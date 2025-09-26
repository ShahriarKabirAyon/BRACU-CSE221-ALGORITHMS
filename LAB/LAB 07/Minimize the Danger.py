import heapq

vertex, edges=map(int, input().split( ))
adj_list={}
for i in range(1, vertex+1):
    adj_list[i]=[]

for i in range(edges):
    u, v, w=map(int, input().split( ))
    adj_list[u].append((v, w))
    adj_list[v].append((u ,w))

danger={}
parent={}
for i in range(1, vertex+1):
    danger[i]=float("inf")

danger[1]=0

heap=[(0,1)]
while heap:
    current_danger, current_city=heapq.heappop(heap)
    if current_danger>danger[current_city]:
        continue
    for neighbor_city, road_danger in adj_list[current_city]:
        new_danger=max(danger[current_city], road_danger)
        if new_danger<danger[neighbor_city]:
            danger[neighbor_city]=new_danger
            heapq.heappush(heap, (new_danger, neighbor_city))

for city in range(1, vertex+1):
    if danger[city]==float("inf"):
        print(-1, end=" ")
    else:
        print(danger[city], end=" ")