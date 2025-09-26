import sys
sys.setrecursionlimit(300000)
A=input().split(" ")
N=int(A[0])
root=int(A[1])

adj_list={}
for i in range(1, N+1):
    adj_list[i]=[]

for i in range(N-1):
    x=input().split(" ")
    u=int(x[0])
    v=int(x[1])
    adj_list[u].append(v)
    adj_list[v].append(u)

size=[0]*(N+1)

def dfs(current, parent):
    size[current]=1
    for adj_node in adj_list[current]:
        if adj_node!=parent:
            dfs(adj_node, current)
            size[current]+=size[adj_node]

dfs(root, None)

number_of_inputs=int(input())
for i in range(number_of_inputs):
    X=int(input())
    print(size[X])