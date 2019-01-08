x2,y2=map(int,input().split(' '))
if x2 > y2:
    great = x2
else:
    great = y2
while(True):
    if((great % x2 == 0) and (great % y2 == 0)):
        lcm = great
        break
    great += 1
print(lcm)
