print("Enter 'x' for exit.");
v = input("Enter year: ");
if v == 'x':
    exit();
try:
    year = int(v);
except ValueError:
    print("Please, enter year...exiting...");
else:
    if((year%4 == 0) and (year%100 != 0)):
        print(year, "is a Leap Year.");
    elseif((year%100 == 0) and (year%400 == 0)):
    	print(year, "is a Leap Year.");
    elseif(year%400 == 0):
    	print(year, "is a Leap Year.");
    else:
    	print(year, "is not a Leap Year.");
