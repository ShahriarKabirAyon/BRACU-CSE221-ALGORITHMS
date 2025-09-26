import sys
sys.setrecursionlimit(2*100000+5)
A=input().split(" ")
N=int(A[0])
M=int(A[1])

U=input().split(" ")
V=input().split(" ")

adj_list={}
for i in range(1, N+1):
    adj_list[i]=[]

for i in range(M):
    u=int(U[i])
    v=int(V[i])
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in adj_list:
    adj_list[i].sort()

visited=[False]*(N+1)
path=[]

def dfs(node):
    visited[node]=True
    path.append(node)
    for i in adj_list[node]:
        if not visited[i]:
            dfs(i)

dfs(1) #starting the visiting from 1 

for i in range(len(path)):
    print(path[i], end=" ")
print()