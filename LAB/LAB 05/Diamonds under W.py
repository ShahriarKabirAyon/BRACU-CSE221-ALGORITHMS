import sys
sys.setrecursionlimit(2000000)

A=input().split(" ")
row=int(A[0])
col=int(A[1])

matrix=[]
visited=[]
r=0
while r<row:
    matrix.append([None]*col)
    visited.append([False]*col)
    r+=1

r=0
while r<row:
    lvl=input()
    c=0
    while c<col:
        matrix[r][c]=lvl[c]
        c+=1
    r+=1

def traversebetweenobstacle(r, c):
    if r<0 or r>=row or c<0 or c>=col:
        return 0
    if visited[r][c] or matrix[r][c]=="#":
        return 0

    visited[r][c]=True
    if matrix[r][c]=="D":
        count=1
    else:
        count=0

    count+=traversebetweenobstacle(r+1, c)
    count+=traversebetweenobstacle(r-1, c)
    count+=traversebetweenobstacle(r, c+1)
    count+=traversebetweenobstacle(r, c-1)

    return count

maximum=0
r=0
while r<row:
    c=0
    while c<col:
        if matrix[r][c]!="#" and not visited[r][c]:
            diamonds=traversebetweenobstacle(r, c)
            if diamonds>maximum:
                maximum=diamonds
        c+=1
    r+=1

print(maximum)