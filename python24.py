v=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    v.append(b)
v.sort(key=len)
print(v)