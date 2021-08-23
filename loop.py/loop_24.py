i=1
a=0
while i<=5:
    num=int(input("enter the weigh"))
    a=a+num
    i=i+1
print("num",a)
if a%5==0:
    print("it is multiple")
else:
    print("it is not multiple")