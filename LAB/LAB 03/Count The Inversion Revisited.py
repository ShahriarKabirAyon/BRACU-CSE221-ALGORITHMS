count=0
def merge(a, b):
    # write your code here
    # a and b are two sorted list
    # merge function will return a sorted list after merging a and b

    global count
    array=[0]*(len(a)+len(b))
    left=0
    right=0
    i=0
    #count=0

    while left<len(a) and right<len(b):
      if a[left]<=b[right]:
        array[i]=a[left]
        left+=1
      else:
        array[i]=b[right]
        maximum=b[right]**2
        L=left
        R=len(a)
        while L<R:
          mid=(L+R)//2
          if a[mid]>maximum:
            R=mid
          else:
            L=mid+1
        count+=(len(a)-L)
        right+=1
      i+=1

    while left<len(a):
      array[i]=a[left]
      i+=1
      left+=1
    while right<len(b):
      array[i]=b[right]
      i+=1
      right+=1

    return array

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)          # complete the merge function above

input()
arr=input().split(" ")
for i in range(len(arr)):
  arr[i]=int(arr[i])

mergeSort(arr)
print(count)