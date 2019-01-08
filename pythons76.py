fd=int(input())
fact=0
for i in range(1,fd):
  if fd%i==0:
    fact=i
if fact>1:
  print ('Yes')
elif fd==1:
  print ('neither prime nor composite')
else:
  print ('No')
