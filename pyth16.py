lower = 900
upper = 1000

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for c in range(lower,upper + 1):
   if c > 1:
       for h in range(2,c):
           if (num % h) == 0:
               break
       else:
           print(c)