j1=input().split()
j1=list(map(int,j))
a2=j[0]
b2=j[1]
c2=a*b
d2=0
if(c!=1):
  for i in range(1,c):
    if((i*i)==c):
     d2=1
  if(d2==1):
    print('yes')
  else:
    print('no')
else:
  print('yes')
