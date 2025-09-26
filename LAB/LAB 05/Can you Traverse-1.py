A=input().split(" ")
N=int(A[0])
M=int(A[1])

adj_list={}
for i in range(1, N+1):
    adj_list[i]=[]

for _ in range(M):
    x=input().split(" ")
    u=int(x[0])
    v=int(x[1])
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(adj_list, sc=1):
    path=[]
    visited=[False]*(N+1)
    queue=[sc]
    visited[sc]=True
    start=0

    while start<len(queue):
        current=queue[start]
        start+=1
        path.append(current)

        for i in sorted(adj_list[current]):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return path

result=bfs(adj_list)
for i in range(len(result)):
    print(result[i], end=" ")
print()