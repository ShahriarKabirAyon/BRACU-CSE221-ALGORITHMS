n=input().split(" ")
array_size=int(n[0])
queries=int(n[1])

array_input=input().split(" ")
array=[]
for i in range(array_size):
  array.append(int(array_input[i]))

for j in range(queries):
  find=input().split(" ")
  lower=int(find[0])
  upper=int(find[1])

  min=0
  max=array_size-1
  lower_pointer=-1

  while min<=max:
    mid=min+(max-min)//2
    if array[mid]>=lower:
      lower_pointer=mid
      max=mid-1
    else:
      min=mid+1

  min=0
  max=array_size-1
  upper_pointer=-1
  while min<=max:
    mid=min+(max-min)//2
    if array[mid]<=upper:
      upper_pointer=mid
      min=mid+1
    else:
      max=mid-1

  if lower_pointer==-1 or upper_pointer==-1 or upper_pointer<lower_pointer:
    print(0)
  else:
    print(upper_pointer-lower_pointer+1)