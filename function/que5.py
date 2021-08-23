def mom(x):
    i=1
    sum=0
    while i<=x:
        if i%3==0:
            print(i)
            sum=sum+i
        if i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum) 
x=int(input("enter the number"))
mom(x)


def mom(a):
    i=1
    s=0
    while i<=a:
        if i%3==0 or i%5==0:
            print(i)
            s=s+i
        i=i+1
    print(s)    
x=int(input("enter the number"))
mom(x)