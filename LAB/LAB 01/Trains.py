N=int(input())
roster={}
for i in range(N):
  info=input().split(" ")
  train=info[0]
  destination=info[4]
  schedule=info[6]
  if train in roster:
    roster[train].append((destination, schedule))
  else:
    roster[train]=[(destination, schedule)]

keys=[]
for i in roster:
  keys.append(i)
for i in range (len(keys)):
  idx=i
  for j in range(i+1, len(keys)):
    if keys[j]<keys[idx]:
      idx=j
  keys[i], keys[idx]=keys[idx], keys[i]

for key in keys:
  for i in range(len(roster[key])):
    for j in range(i+1, len(roster[key])):
      if roster[key][i][1]<roster[key][j][1]:
        roster[key][i], roster[key][j]=roster[key][j], roster[key][i]

  for i in range(len(roster[key])):
    print(f"{key} will departure for {roster[key][i][0]} at {roster[key][i][1]}")