A=input().split(" ")
N=int(A[0])
M=int(A[1])

graph={}
for i in range(1, N+1):
    graph[i]=[]

for i in range(M):
    X=input().split(" ")
    u=int(X[0])
    v=int(X[1])
    graph[u].append(v)
    graph[v].append(u)

def bipartite(graph, N):
    tackles={}
    for i in range(1, N+1):
        tackles[i]=-1

    queue=[]
    head=0
    result=0

    for j in range(1, N+1):
        if tackles[j]==-1:
            zeros=0
            ones=0
            queue.append(j)
            tackles[j]=1
            ones+=1

            while head<len(queue):
                current=queue[head]
                head+=1
                for k in graph[current]:
                    if tackles[k]==-1:
                        if tackles[current]==1:
                            tackles[k]=0
                            zeros+=1
                        else:
                            tackles[k]=1
                            ones+=1
                        queue.append(k)
            result+=max(zeros, ones)

    return result
answer=bipartite(graph, N)
print(answer)