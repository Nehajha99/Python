def num(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            print(i)
            count=count+1
        i=i+1
    if count==2:
        return"prime number"
    else:
        return"not prime number"              
x=int(input("enter the number"))
print(num(x))    