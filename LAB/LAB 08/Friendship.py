def union(x, y, parent, size):
    root1=x
    while parent[root1]!=root1:
        parent[root1]=parent[parent[root1]]
        root1=parent[root1]

    root2=y
    while parent[root2]!=root2:
        parent[root2]=parent[parent[root2]]
        root2=parent[root2]

    if root1==root2:
        return size[root1]

    if size[root1]<size[root2]:
        root1, root2 = root2, root1
    parent[root2]=root1
    size[root1]+=size[root2]

    return size[root1]

N, K=map(int, input().split( ))

parent={}
size={}
for i in range(1, N+1):
    parent[i]=i
    size[i]=1

for i in range(K):
    friend1, friend2=map(int, input().split())
    print(union(friend1, friend2, parent, size))