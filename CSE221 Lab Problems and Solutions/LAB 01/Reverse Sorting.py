N=int(input())
array=input().split(" ")
for i in range(len(array)):
  array[i]=int(array[i])

i1=array[1::2]
flag=True
while flag:
  flag=False
  for i in range(len(i1)-1):
    if i1[i]>i1[i+1]:
      i1[i], i1[i+1]=i1[i+1], i1[i]
      flag=True

i2=array[0::2]
flag=True
while flag:
  flag=False
  for i in range(len(i2)-1):
    if i2[i]>i2[i+1]:
      i2[i], i2[i+1]=i2[i+1], i2[i]
      flag=True

merged=[]
for i in range(len(array)):
  if i%2==0:
    merged.append(i2[i//2])
  else:
    merged.append(i1[i//2])

flag=True
while flag:
  flag=False
  for i in range(len(array)-1):
    if array[i]>array[i+1]:
      array[i], array[i+1]=array[i+1], array[i]
      flag=True

flag=True
for i in range(len(merged)):
  if merged[i]!=array[i]:
    flag=False
    break

if flag==True:
  print("Yes")
else:
  print("No")