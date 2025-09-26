n=int(input())
a=input().split(" ")
for i in range(len(a)):
    a[i]=int(a[i])

start=(a[0]-1, a[1]-1)
end=(a[2]-1, a[3]-1)
moves=[(-2, -1), (-2, 1), (-1, 2), (1, 2),
        (2, 1), (2, -1), (1, -2), (-1, -2)]
dist=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(-1)
    dist.append(row)

dist[start[0]][start[1]]=0
q=[None]*(n*n)
q[0]=start
head=0
tail=1

result=-1
while head<tail:
    x, y=q[head]
    head+=1
    if (x, y)==end:
        result=dist[x][y]
        break
    for dx, dy in moves:
        nx, ny=x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
            dist[nx][ny]=dist[x][y]+1
            q[tail]=(nx, ny)
            tail+=1

print(result)