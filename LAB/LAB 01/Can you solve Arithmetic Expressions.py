T = int(input())
if 1<=T and T<=1000:
  for i in range(T):
    N = (input())
    NN = N.split(" ")
    a=float(NN[1])
    b=float(NN[3])
    if NN[2]=="+":
      print(a+b)
    elif NN[2]=="/":
      print(a/b)
    elif NN[2]=="-":
      print(a-b)
    elif NN[2]=="*":
      print(a*b)