import sys
sys.setrecursionlimit(2*100000+5)
A=input().split(" ")
N=int(A[0])
M=int(A[1])

adj_list={}
for i in range(1, N+1):
    adj_list[i]=[]

for i in range(M):
    x=input().split(" ")
    u=int(x[0])
    v=int(x[1])
    adj_list[u].append(v)

visited=[0]*(N+1)

def dfs(u):
    visited[u]=1
    for v in adj_list[u]:
        if visited[v]==0:
            if dfs(v):
                return True
        elif visited[v]==1:
            return True
    visited[u]=2   
    return False

cycled=False    
for i in range(1, N+1):
    if visited[i]==0:
        if dfs(i):
            cycled=True
            break
if cycled:
    print("YES")
else:
    print("NO")