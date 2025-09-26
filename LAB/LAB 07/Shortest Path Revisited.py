import heapq

v, e, s, d=map(int, input().split( ))
adj={}
for i in range(1, v+1):
    adj[i]=[]

for i in range(e):
    x, y, w=map(int, input().split( ))
    adj[x].append((y, w))
    adj[y].append((x, w))

dist={}
for i in range(1, v+1):
    dist[i]=[float("inf"), float("inf")]

dist[s][0]=0

heap=[]
heapq.heappush(heap, (0, s))

while len(heap)>0:
    current_distance,current_node=heapq.heappop(heap)
    for neighbour, weight in adj[current_node]:
        new_distance=current_distance+weight
        if new_distance<dist[neighbour][0]:
            dist[neighbour][1]=dist[neighbour][0]
            dist[neighbour][0]=new_distance
            heapq.heappush(heap, (new_distance, neighbour))
        elif dist[neighbour][0]<new_distance<dist[neighbour][1]:
            dist[neighbour][1]=new_distance
            heapq.heappush(heap, (new_distance, neighbour))

if dist[d][1]==float("inf"):
    print(-1)
else:
    print(dist[d][1])