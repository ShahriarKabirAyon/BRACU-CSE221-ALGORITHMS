input()
id=input().split(" ")
marks=input().split(" ")
for i in range (len(id)):
  id[i]=int(id[i])
  marks[i]=int(marks[i])

array=[]
for i in range(len(id)):
  array.append((marks[i], id[i]))

count=0
for i in range(len(array)):
  idx=i
  for j in range(i+1, len(array)):
    if (array[j][0]>array[idx][0]) or (array[j][0]==array[idx][0] and array[j][1]<array[idx][1]):
      idx=j
  if idx!=i:
    array[i], array[idx]=array[idx], array[i]
    count+=1

print(f"Minimum swaps: {count}")
for i in range(len(array)):
  print(f"ID: {array[i][1]} Mark: {array[i][0]}")