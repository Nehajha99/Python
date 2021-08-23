num=int(input("enter the number"))
i=1
s=0
while num>=i:
    if num%i==0:
        print(i,"factor")
        s=s+1
    i=i+1
if s==2:
    print(num,"prime number")
else:
    print(num,"not prime number")       


        