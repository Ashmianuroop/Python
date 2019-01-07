l=int(input("enter the no"))
h=int(input("enter the no"))
j=[]
for i in range(0,l):
    h=int(input("enter"))
    j.append(h)
print(j.count(h))
if(j.count(h)==0):
    print("k is not here")
