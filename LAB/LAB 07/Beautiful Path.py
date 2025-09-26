import heapq

vertex_edge_source_destination=input().split( )
vertex=int(vertex_edge_source_destination[0])
edge=int(vertex_edge_source_destination[1])
source=int(vertex_edge_source_destination[2])
destination=int(vertex_edge_source_destination[3])

weights_input=input().split( )
weights=[]
for i in range(vertex):
    weights.append(int(weights_input[i]))

adj_list={}
for i in range(1, vertex+1):
    adj_list[i]=[]

for i in range(edge):
    src_dest=input().split( )
    src=int(src_dest[0])
    dest=int(src_dest[1])
    adj_list[src].append(dest)

minimum_cost={}
for i in range(1, vertex+1):
    minimum_cost[i]=float("inf")

minimum_cost[source]=weights[source-1]

heap=[]
heapq.heappush(heap, (minimum_cost[source],source))

while len(heap)>0:
    current_pair=heapq.heappop(heap)
    current_cost=current_pair[0]
    current_node=current_pair[1]

    if current_cost>minimum_cost[current_node]:
        continue

    neighbors=adj_list[current_node]
    for i in range(len(neighbors)):
        neighbor=neighbors[i]
        new_cost=current_cost+weights[neighbor-1]
        if new_cost<minimum_cost[neighbor]:
            minimum_cost[neighbor]=new_cost
            heapq.heappush(heap, (new_cost, neighbor))

if minimum_cost[destination]==float("inf"):
    print(-1)
else:
    print(minimum_cost[destination])