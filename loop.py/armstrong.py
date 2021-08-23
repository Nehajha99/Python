n=int(input("enter the number"))
b=n
arm=0
i=0
count=0
while n>i:
    count=count+1
    n=n//10
print(count)
j=b
while j>0:
    s=j%10
    arm=arm+s**count
    j=j//10
print(arm)
if arm==b:
    print("yes")
else:
    print("no")        

