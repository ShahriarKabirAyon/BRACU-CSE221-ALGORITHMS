T=int(input())
for i in range(T):
  array=input().split(" ")
  k=int(array[0])
  x=int(array[1])

  left=1
  right=2*k

  while left<right:
    mid=left+((right-left)//2)
    Counter=mid-(mid//x)

    if Counter<k:
      left=mid+1
    else:
      right=mid
  print(left)