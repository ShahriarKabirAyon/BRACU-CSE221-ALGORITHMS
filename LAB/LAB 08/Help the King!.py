def sort(array):
    length=len(array)  
    if length==1:
        return array 

    mid=length//2
    L=array[:mid]
    R=array[mid:]

    L=sort(L)
    R=sort(R)
    left, right=0, 0
    left_length=len(L)
    right_length=len(R)

    sorted_array=[0]*length
    i=0
    while left<left_length and right<right_length:
        if L[left][2]<R[right][2]:
            sorted_array[i]=L[left]
            left+=1
        else:
            sorted_array[i]=R[right]
            right+=1  
        i+=1
    
    while left<left_length:
        sorted_array[i]=L[left]
        left+=1
        i+=1
    
    while right<right_length:
        sorted_array[i]=R[right]
        right+=1
        i+=1
    
    return sorted_array


def minimumCost(edges, vertex):
    parent=[0]*(vertex+1)
    size=[0]*(vertex+1)
    for i in range(vertex+1):
        parent[i]=i
        size[i]=1
    
    edges=sort(edges)
    cost=0
    for u, i, w in edges:
        rootU=u
        while parent[rootU]!=rootU:
            parent[rootU]=parent[parent[rootU]]
            rootU=parent[rootU]

        rootV=i
        while parent[rootV]!=rootV:
            parent[rootV]=parent[parent[rootV]]
            rootV=parent[rootV]

        if rootU!=rootV:
            if size[rootU]<size[rootV]:
                rootU, rootV=rootV, rootU
            parent[rootV]=rootU
            size[rootU]+=size[rootV]
            cost+=w            
    return cost

vertex, edge=map(int, input().split( ))
edges=[]

for i in range(edge):
    source, destination, weight=map(int, input().split( ))
    edges.append((source, destination, weight))

print(minimumCost(edges, vertex))