def evan(a):
    i=0
    while i<=a:
        if i%2==0:
            print("evan number=",i)
        else:
            print("odd number=",i)
        i=i+1
num=int(input("enter the number"))    
evan(num)   