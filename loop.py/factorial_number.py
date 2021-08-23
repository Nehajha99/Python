#####factorial number
###4=4*3*2*1=24

a=int(input("enter the number"))
m=1
while a>=1:
    print(a,"*",end="")
    m=m*a
    a=a-1
print("=",m)    