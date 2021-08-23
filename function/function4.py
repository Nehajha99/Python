def add_number(num1,num2):
    num3=num1+num2
    print("add=",num3)
num1=56
num2=12
add_number(num1,num2)
    
def add_number(num1,num2):
    i=0
    j=0
    while i<len(num1) and j<len(num2):
        num3=num1[i]+num2[j]
        print("add=",num3)
        j=j+1
        i=i+1
a=[50,60,10]
b=[10,20,13]
add_number(a,b)
