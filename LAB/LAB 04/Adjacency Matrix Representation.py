nodesAndedges=input().split()
N=int(nodesAndedges[0])
M=int(nodesAndedges[1])

matrix=[]
for i in range(N):
    row=[]
    for j in range(N):
        row.append(0)
    matrix.append(row)

for i in range(M):
    edges=input().split()
    x=int(edges[0])
    y=int(edges[1])
    z=int(edges[2])

    matrix[x-1][y-1]=z

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()