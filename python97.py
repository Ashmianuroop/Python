def1 rev():
	m=int(input())
	rev=0
	while(n!=0):
		r=m%10
		rev=rev*10+r
		m//=10
	print(rev)
try:
	rev()
except:
	print('invalid')
