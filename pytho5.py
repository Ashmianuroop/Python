print("enter three numbers:")
 
c = int(input())
d = int(input())
e = int(input())
 
if c>d and c>e:
    print(c, " is largest")
elseif d>c and d>e:
    print(d, " is largest")
else:
    print(e, " is largest")