N=input().split(" ")
length=int(N[0])
K=int(N[1])

input_array=input().split(" ")
array=[]
for i in range(length):
  array.append(int(input_array[i]))

i=0
max=0
sum=0
for j in range(length):
  sum+=array[j]
  while sum>K and i<=j:
    sum-=array[i]
    i=i+1
  
  if (j-i+1)>max:
    max=(j-i+1)

print(max)