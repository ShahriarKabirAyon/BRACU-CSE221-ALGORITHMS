T=int(input())
if 1<=T and T<=100:
    for i in range (T):
        N=int(input())
        if -10**5<=N and N<=10**5:
            if N%2==0:
                print(f"{N} is an Even number.")
            else:
                print(f"{N} is an Odd number.")