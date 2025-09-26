K=int(input().split(" ")[1])
array=input().split(" ")
for i in range(len(array)):
  array[i]=int(array[i])

maximum=(2*10**5)+1
hashTable=[0]*maximum
maxLength=0
left=0
count=0

for i in range(len(array)):
  hashTable[array[i]]+=1
  if hashTable[array[i]]==1:
    count+=1
  while count>K:
    hashTable[array[left]]-=1
    if hashTable[array[left]]==0:
      count-=1
    left+=1

  if i-left+1>maxLength:
    maxLength=i-left+1

print(maxLength)