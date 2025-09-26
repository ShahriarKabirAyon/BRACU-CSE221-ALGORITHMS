import sys
sys.setrecursionlimit(3000)

def disjointSet(size):
    parent=[]
    for i in range(size+1):
        parent.append(i)
    rank=[]
    for i in range(size+1):
        rank.append(0)
    return parent, rank

def find(parent, node):
    if parent[node]!=node:
        parent[node]=find(parent, parent[node])
    return parent[node]

def union(parent, rank, u, v):
    ru=find(parent, u)
    rv=find(parent, v)
    if ru==rv:
        return False
    if rank[ru]<rank[rv]:
        ru, rv=rv, ru
    parent[rv]=ru
    if rank[ru]==rank[rv]:
        rank[ru]+=1
    return True

def pair(a, b):
    vals=[a[0], a[1], b[0], b[1]]
    f=[]
    for i in vals:
        if i!=-10**12:
            f.append(i)
    d=[]
    for i in f:
        if i not in d:
            d.append(i)

    for i in range(len(d)):
        for j in range(i+1, len(d)):
            if d[j]>d[i]:
                d[i], d[j]=d[j], d[i]
    if len(d)>0:
        first=d[0]
    else:
        first=-10**12
    if len(d)>1:
        second=d[1]
    else:
        second=-10**12
    return(first, second)

def DFS(node, parent, w, g, anc, m1, m2, dep):
    anc[0][node]=parent
    if parent != 0:
        m1[0][node] = w
    else:
        m1[0][node] = -10**12
    for nei, wei in g[node]:
        if nei==parent:
            continue
        dep[nei]=dep[node]+1
        DFS(nei, node, wei, g, anc, m1, m2, dep)

def gather(node, steps, mj, anc, m1, m2):
    res=(-10**12, -10**12)
    for k in range(mj):
        if(steps>>k)&1:
            res=pair(res, (m1[k][node], m2[k][node]))
            node=anc[k][node]
    return node, res

def bestEdge(u, v, w, dep, mj, anc, m1, m2):
    acc=(-10**12, -10**12)
    if dep[u]<dep[v]:
        temp=u
        u=v
        v=temp
    u, res=gather(u, dep[u]-dep[v], mj, anc, m1, m2)
    acc=pair(acc, res)
    if u==v:
        a, b=acc
        if a<w:
            return a
        if b<w:
            return b
        return -10**12
    for k in range(mj-1, -1, -1):
        if anc[k][u]!=anc[k][v]:
            acc=pair(acc, (m1[k][u], m2[k][u]))
            acc=pair(acc, (m1[k][v], m2[k][v]))
            u=anc[k][u]
            v=anc[k][v]
    acc=pair(acc, (m1[0][u], m2[0][u]))
    acc=pair(acc, (m1[0][v], m2[0][v]))
    a, b=acc
    if a<w:
        return a
    if b<w:
        return b
    return -10**12

def mergeSort(e):
    if len(e)<=1:
        return e
    mid=len(e)//2
    left=mergeSort(e[:mid])
    right=mergeSort(e[mid:])
    m=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i][2]<=right[j][2]:
            m.append(left[i])
            i+=1
        else:
            m.append(right[j])
            j+=1
    for x in left[i:]:
        m.append(x)
    for x in right[j:]:
        m.append(x)
    return m

n, m=map(int, input().split())
edges=[]
for _ in range(m):
    values=input().split()
    temp=[]
    for v in values:
        temp.append(int(v))
    temp.append(False)
    edges.append(temp)

parent, rank=disjointSet(n)
edges=mergeSort(edges)
mst_cost=0
mst_edges_used=0
graph=[]
for i in range(n+1):
    graph.append([])

for u, v, w, x in edges:
    if union(parent, rank, u, v):
        mst_cost+=w
        mst_edges_used+=1
        graph[u].append((v, w))
        graph[v].append((u, w))
        for e in edges:
            if e[0]==u and e[1]==v and e[2]==w and not e[3]:
                e[3]=True
                break

if mst_edges_used!=n-1:
    print(-1)
else:
    mj=(n).bit_length()
    anc=[]
    for i in range(mj):
        anc.append([0]*(n+1))
    m1=[]
    for i in range(mj):
        m1.append([-10**12]*(n+1))
    m2=[]
    for i in range(mj):
        m2.append([-10**12]*(n+1))
    dep=[0]*(n+1)
    DFS(1, 0, -10**12, graph, anc, m1, m2, dep)

    for k in range(1, mj):
        for node in range(1, n+1):
            anc[k][node]=anc[k-1][anc[k-1][node]]
            p=pair((m1[k-1][node], m2[k-1][node]), (m1[k-1][anc[k-1][node]], m2[k-1][anc[k-1][node]]))
            m1[k][node], m2[k][node]=p

    ans=float("inf")
    for u, v, w, in_mst in edges:
        if in_mst:
            continue
        best=bestEdge(u, v, w, dep, mj, anc, m1, m2)
        if best!=-10**12:
            cand=mst_cost+w-best
            if cand<ans:
                ans=cand

    if ans==float("inf"):
        print(-1)
    else:
        print(ans)