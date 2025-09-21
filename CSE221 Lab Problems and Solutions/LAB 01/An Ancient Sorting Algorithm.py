input()
N=input().split(" ")
for i in range (len(N)):
  N[i]=int(N[i])

flag=True
while flag:
  flag=False
  for i in range(len(N)-1):
    if N[i]%2==0 and N[i+1]%2==0 and N[i]>N[i+1]:
      N[i],N[i+1]=N[i+1],N[i]
      flag=True
    elif N[i]%2!=0 and N[i+1]%2!=0 and N[i]>N[i+1]:
      N[i],N[i+1]=N[i+1],N[i]
      flag=True
for j in range (len(N)):
  print(N[j], end=" ")