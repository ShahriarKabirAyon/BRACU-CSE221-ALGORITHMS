N=input().split()
length=int(N[0])
sum=int(N[1])

array=[]
arr=input().split()
for i in arr:
  array.append(int(i))

i=0
j=length-1
flag=False
while i<j:
  if array[i]+array[j]==sum:
    print(f"{i+1} {j+1}")
    flag=True
    break
  elif array[i]+array[j]<sum:
    i+=1
  elif array[i]+array[j]>sum:
    j-=1
if flag==False:
  print("-1")