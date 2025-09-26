N=int(input().split(" ")[1])
X=input().split(" ")
for i in range(len(X)):
  X[i]=int(X[i])
for j in range(len(X)):
  X[j]=(X[j],j)

X.sort()
trios=None

for i in range(len(X)):
  left=i+1
  right=len(X)-1
  sum=0
  while left<right:
    sum=X[i][0]+X[left][0]+X[right][0]
    if sum==N:
      result=[1+X[i][1], 1+X[left][1], 1+X[right][1]]
      result.sort()
      if trios==None or result<trios:
        trios=result
      left+=1
      right-=1
    elif sum<N:
      left+=1
    else:
      right-=1

if trios!=None:
  print(*trios)
else:
  print(-1)