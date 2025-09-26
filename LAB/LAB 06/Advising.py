A=input().split(" ")
v=int(A[0])
e=int(A[1])

graph={}
indegree={}

for i in range(1, v+1):
    graph[i]=[]
    indegree[i]=0

edges=[]
for i in range(e):
    x=input().split(" ")
    a=int(x[0])
    b=int(x[1])
    graph[a].append(b)
    indegree[b]+=1
    edges.append((a, b))

def topsort(graph, indegree, v):
    queue=[]
    head=0
    path=[]

    visited=[0]*(v+1)
    for a, b in edges:
        if indegree[a]==0 and visited[a]==0:
            queue.append(a)
            visited[a]=1
        if indegree[b]==0 and visited[b]==0:
            queue.append(b)
            visited[b]=1

    for i in range(1, v+1):
        if indegree[i]==0 and visited[i]==0:
            queue.append(i)
            visited[i]=1

    while head<len(queue):
        current=queue[head]
        head+=1
        path.append(current)
        for j in graph[current]:
            indegree[j]-=1
            if indegree[j]==0 and visited[j]==0:
                queue.append(j)
                visited[j]=1

    if len(path)!=v:
        return [-1]
    return path

result=topsort(graph, indegree, v)
for i in result:
    print(i, end=" ")