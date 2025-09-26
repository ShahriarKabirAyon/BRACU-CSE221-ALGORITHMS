import heapq

vertex, edge, S, T=map(int, input().split( ))
adj_list={}
for i in range(1, vertex+1):
    adj_list[i]=[]
for i in range(edge):
    u, v, w=map(int, input().split( ))
    adj_list[u].append((v, w))

def Dijkstra(source):
    distances={}
    for i in range(1, vertex+1):
        distances[i]=float("inf")
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
                heapq.heappush(heap, (new_distance, neighbor))
    return distances

distances_A=Dijkstra(S)
distances_B=Dijkstra(T)

min_meet_time=float("inf")
mutual=-1
for node in adj_list:
    if distances_A[node]!=float("inf") and distances_B[node]!=float("inf"):
        curr_meet_time=max(distances_A[node], distances_B[node])
        if curr_meet_time<min_meet_time:
            min_meet_time=curr_meet_time
            mutual=node
        elif curr_meet_time==min_meet_time:
            mutual=min(mutual, node)

if mutual==-1:
    print(-1)
else:
    print(min_meet_time, mutual)