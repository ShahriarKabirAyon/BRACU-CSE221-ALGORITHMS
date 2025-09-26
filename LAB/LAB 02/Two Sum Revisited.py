K=int(input().split(" ")[2])
N=input().split(" ")
for i in range(len(N)):
  N[i]=int(N[i])
M=input().split(" ")
for j in range(len(M)):
  M[j]=int(M[j])

left=0
right=len(M)-1


highest_difference=9999999999
b_left=0
b_right=0

sum=0
flag=False
while left<len(N) and right>=0:
  sum=N[left]+M[right]
  difference=abs(sum-K)
  if difference<highest_difference:
    highest_difference=difference
    b_left=left
    b_right=right

  if sum==K:
    print(b_left+1, b_right+1)
    flag=True
    break
  elif sum<K:
    left+=1
  else:
    right-=1

if flag==False:
  print(b_left+1, b_right+1)