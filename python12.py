s=int(raw_input("Enter a number"))
sum1=0
c=s
 
while s!=0:
	rem=s%10
	sum1=sum1*10+rem
	s=s/10
if sum1==c:
	print c, "is palindrome"
else:
	print c, "is not palindrome"