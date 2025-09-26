A=input().split(" ")
n=int(A[0])
m=int(A[1])
s=int(A[2])
d=int(A[3])

graph={}
for i in range(1, n+1):
    graph[i]=[]

list1=input().split(" ")
list2=input().split(" ")

for i in range(m):
    u=int(list1[i])
    v=int(list2[i])
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

distance=[pow(10,9)]*(n+1)
parent=[-1]*(n+1)
distance[s]=0
parent[s]=None

queue=[0]*(n+5)
front=0
back=0
queue[back]=s
back+=1

while front<back:
    current=queue[front]
    front+=1
    for j in range(len(graph[current])):
        neighbor=graph[current][j]
        if distance[neighbor]>distance[current] + 1:
            distance[neighbor]=distance[current] + 1
            parent[neighbor]=current
            queue[back]=neighbor
            back+=1

if distance[d]==pow(10,9):
    print("-1")
else:
    path=[]
    current=d
    while current!=None:
        path.append(current)
        current=parent[current]
    print(len(path)-1)
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=" ")
    print()