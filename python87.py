x7,y5=map(int,input().split(' '))
if x7 > y5:
    smaller = y5
else:
    smaller = x7
for i in range(1, smaller+1):
    if((x7 % i == 0) and (y5 % i == 0)):gcd1 = i
print(gcd1)
