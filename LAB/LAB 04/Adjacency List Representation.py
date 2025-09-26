nodesAndedges=input().split()
N=int(nodesAndedges[0])
M=int(nodesAndedges[1])

u=input().split()
v=input().split()
w=input().split()

for i in range(M):
    u[i]=int(u[i])
for i in range(M):
    v[i]=int(v[i])
for i in range(M):
    w[i]=int(w[i])

list={}
for i in range(1, N+1):
    list[i]=[]
for i in range(M):
    list[u[i]].append((v[i],  w[i]))

for i in range(1, N+1):
    print(f"{i}:", end=" ")
    for j in list[i]:
        print(f"({j[0]},{j[1]})", end=" ")
    print()