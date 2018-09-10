lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for n in range(lower,upper + 1):
  
   value = 0
 
   temp = n
   while temp > 0:
       digit = temp % 10
       value += digit ** 3
       temp //= 10
 
   if n == sum:
       print(n)