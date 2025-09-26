N1=int(input())
array1=list(map(int, input().split()))
N2=int(input())
array2=list(map(int, input().split()))

i=0
j=0
array3=[]
while i<N1 and j<N2:
    if array1[i]<=array2[j]:
        array3.append(array1[i])
        i+=1
    else:
        array3.append(array2[j])
        j+=1
while i<N1:
    array3.append(array1[i])
    i+=1
while j<N2:
    array3.append(array2[j])
    j+=1
for i in array3:
    print(i, end=" ")
print()