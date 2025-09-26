A=input().split(" ")
n=int(A[0])
m=int(A[1])
s=int(A[2])
d=int(A[3])
k=int(A[4])

graph=[]
for i in range(n+1):
    graph.append([])

for i in range(m):
    x=input().split(" ")
    u=int(x[0])
    v=int(x[1])
    graph[u].append(v)

for i in range(1, n+1):
    graph[i].sort()

def bfs(start):
    distance=[]
    parent=[]
    for i in range(n+1):
        distance.append(pow(10,9))
        parent.append(-1)

    distance[start]=0
    parent[start]=0

    q=[]
    q.append(start)
    head=0

    while head<len(q):
        current=q[head]
        head+=1
        for i in graph[current]:
            if distance[i]>distance[current]+1:
                distance[i]=distance[current]+1
                parent[i]=current
                q.append(i)

    return distance, parent

distance1, parent1=bfs(s)
if distance1[k]==pow(10,9):
    print("-1")
    exit()

path1=[]
current=k
while current!=0:
    path1.append(current)
    current=parent1[current]
path1.reverse()

distance2, parent2=bfs(k)
if distance2[d]==pow(10,9):
    print("-1")
    exit()

path2=[]
current=d
while current!=0:
    path2.append(current)
    current= parent2[current]
path2.reverse()

result=[]
for i in path1:
    result.append(i)
for i in range(1, len(path2)):
    result.append(path2[i])

print(len(result)-1)
for i in result:
    print(i, end=" ")