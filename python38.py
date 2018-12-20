a = a ^ b
b = a ^ b
 
print("before swapping\na=", a, " b=", b)
 
temp = a
a = b
b = temp
 
print("\nafter swapping\na=", a, " b=", b)

