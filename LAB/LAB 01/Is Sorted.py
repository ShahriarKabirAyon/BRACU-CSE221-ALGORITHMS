T=int(input())
if 1<=T and T<=100:
    for i in range (T):
        input()
        N=input()
        array=N.split( )
        flag=True
        for j in range (len(array)-1):
            if int(array[j])>int(array[j+1]):
                flag=False
        
        if flag==True:
            print("YES")
        else:
            print("NO")