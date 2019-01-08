n5=int(input("Enter integer:"))
if(n5>1):
  for i in range(2,n5):
    if(n5%i)==0:
      print("it is not prime number")
      break;
    else:
      print("It is prime number")
      break;
else:
  print("not prime number")
