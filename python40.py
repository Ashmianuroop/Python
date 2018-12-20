y=int(input("enter no. of terms"))
    a1=0
    b2=1
    count=0
    if(y==0):
        print(a1)
    elif(y<0):
        print("enter  valid number")
    else:
        while(count<y):
            print(a1)
            nexterm= a1+b2
            a1=b2
            b2=nexterm
            count+=1
