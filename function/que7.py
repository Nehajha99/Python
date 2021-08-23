def sajan(a,b):
    if len(a)<len(b):
        print(b)
    elif len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print(a,b)    
x=input("enter the name")
y=input("enter the name")
sajan(x,y)