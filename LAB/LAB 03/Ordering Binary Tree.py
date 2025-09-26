def binaryTree(array, left, right, result):
    if left>right:
        return -1
    mid=(left+right)//2
    result.append(array[mid])

    binaryTree(array, left, mid-1, result)
    binaryTree(array, mid+1, right, result)

array_size=int(input())
array=input().split(" ")
for i in range(array_size):
    array[i]=int(array[i])

result=[]
binaryTree(array, 0, array_size-1, result)

for i in result:
    print(i, end=" ")