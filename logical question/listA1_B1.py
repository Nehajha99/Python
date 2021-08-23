num=int(input("enter the number"))
list1=["A","B"]
a=[]
i=1
while i<=num:
    num1=i
    j=0
    while j<len(list1):
        b=list1[j]+str(num1)
        a.append(b)
        j=j+1
    i=i+1
print(a)    
 