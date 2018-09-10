f = int(input("Enter any number: "))
if f > 1:
    for i in range(2, f):
        if (f % i) == 0:
            print(f, "is not a prime number")
            break
    else:
        print(f, "is a prime number")
else:
    print(f, "is not a prime number")