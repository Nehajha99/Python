# perfact number......
def per(a):
    i=1
    mul=1
    while i<a:
        if a%i==0:
            mul=mul*i
        i=i+1
    if mul==a:
        print("perfect number")
    else:
        print("not perfect number")
x=int(input("enter the number"))
per(x)    

