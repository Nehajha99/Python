# what is fibonacci series....
# 0+1=1
# 1+2=3
# 2+3=5
# 3+5=8
num=int(input("enter the number"))
a=0
b=1
sum1=0
i=1
while i<=num:
    print(sum1)
    i=i+1
    a=b
    b=sum1
    sum1=a+b