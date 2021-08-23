def speed(a):
    if a<70:
        print("ok")
    else:
        i=70
        count=0
        while i<a:
            count=count+1
            i=i+1
        point=count//5
        if point>12:
            return "License suspended"  
        print(point)
        print("he can drive")
x=int(input("enter the number"))
print(speed(x))               
