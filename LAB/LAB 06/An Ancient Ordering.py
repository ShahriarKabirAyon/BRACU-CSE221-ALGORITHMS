N=int(input())

words=[]
for i in range(N):
    words.append(input())

unique_characters=[]
for i in words:
    for j in i:
        if j not in unique_characters:
            unique_characters.append(j)

graph={}
indegree={}
for i in unique_characters:
    graph[i]=[]
    indegree[i]=0

flag=True
for i in range(N-1):
    w1=words[i]
    w2=words[i+1]
    minimum=min(len(w1), len(w2))

    if len(w1)>len(w2) and w1[:minimum]==w2[:minimum]:
        flag=False
        break

    for j in range(minimum):
        if w1[j]!=w2[j]:
            a=w1[j]
            b=w2[j]
            if b not in graph[a]:
                graph[a].append(b)
                indegree[b]+=1
            break

if not flag:
    print(-1)
else:
    order=[]
    q=[]
    for k in unique_characters:
        if indegree[k]==0:
            q.append(k)

    count=0
    while q:
        q.sort()
        node=q[0]
        q=q[1:]

        order.append(node)
        count+=1

        for i in graph[node]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    if count!=len(unique_characters):
        print(-1)
    else:
        for c in order:
            print(c, end="")