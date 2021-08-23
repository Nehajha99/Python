a=5
i=1
c=5
while i<=5:
    n=int(input("enter the password"))
    if n>=1 and n<=10:
        if n==5:
            print("your password is correct")
            break
        elif n!=5:
            print("your guessing worng")
            b=c-i
            print("your remaining chance",b)  
            if b==0:
                print("you are not able to gusse number")
                print("game over")
    else:            
        print("you are enter invalid number")
        break
    i=i+1            
