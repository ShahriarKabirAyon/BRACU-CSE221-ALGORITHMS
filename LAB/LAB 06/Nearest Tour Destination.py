A=input().split(" ")
n=int(A[0])
m=int(A[1])
s=int(A[2])
q=int(A[3])

adj={}
for i in range(1,n+1):
    adj[i]=[]

for i in range(m):
    x=input().split(" ")
    u=int(x[0])
    v=int(x[1])
    adj[u].append(v)
    adj[v].append(u)

start=input().split(" ")
for i in range(len(start)):
    start[i]=int(start[i])

end=input().split(" ")
for i in range(len(end)):
    end[i]=int(end[i])

dist=[]
for i in range(n+1):
    dist.append(-1)

queue=[]
for i in start:
    dist[i]=0
    queue.append(i)

p=0
while p<len(queue):
    u=queue[p]
    for v in adj[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            queue.append(v)
    p+=1

for i in end:
    print(dist[i],end=" ")