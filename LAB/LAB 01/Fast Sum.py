T=int(input())
if 1<=T and T<=10**4:
  for i in range (T):
    N=int(input())
    if 1<=N and N<=10**6:
      print(int((N*(N+1))/2))