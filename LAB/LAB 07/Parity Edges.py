import heapq

vertex, edge=map(int, input().split( ))
src=list(map(int, input().split( )))
dest=list(map(int, input().split( )))
weights=list(map(int, input().split( )))

adj_list={}
for i in range(1, vertex+1):
    adj_list[i]=[]

for i in range(len(src)):
    adj_list[src[i]].append((dest[i], weights[i]))

distance={}
for i in adj_list:
    distance[i]={}
    distance[i][True]=float("inf")
    distance[i][False]=float("inf")

distance[1][True]=0
distance[1][False]=0

heap=[]
heapq.heappush(heap, (0, 1, None))

while len(heap)>0:
    current_distance, current_node, last_edge_parity=heapq.heappop(heap)
    if last_edge_parity!=None and current_distance>distance[current_node][last_edge_parity]:
        continue
    for neighbour, weight in adj_list[current_node]:
        even=(weight%2==0)
        if last_edge_parity==None or last_edge_parity!=even:
            if current_distance+weight<distance[neighbour][even]:
                distance[neighbour][even]=current_distance+weight
                heapq.heappush(heap, (distance[neighbour][even], neighbour, even))

ans=min(distance[vertex][True], distance[vertex][False])
if ans==float("inf"):
    print(-1)
else:
    print(ans)