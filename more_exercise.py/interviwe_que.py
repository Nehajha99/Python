#####que 2
# name=["snowball","chewy","bubbles","gruff"]
# animal=["cat","dog","fish","goat"]
# age=[1,2,2,6]
# i=0
# while i<len(name) and i<len(animal) and i<len(age):
#     print(name[i],"the",animal[i],"is",age[i])
#     i=i+1

# name=["snowball","chewy","bubbles","gruff"]
# animal=["cat","dog","fish","goat"]
# age=[1,2,2,6]
# index=0
# while index<len(name):
#     print(name[index],"the",animal[index],"is",age[index])
#     index=index+1


###Default parameter value we use here
# def func(message,num=1):
#     print(message*num)
# func("welcome")
# func("viewers",3)    

###Expended_form
# n=int(input("enter the number"))
# i=1
# sum1=0
# while i<=n:
#     sum1=sum1+i
#     print(i-1,"+",end="")
#     i=i+1
# print(n,end="")
# print("=",sum1)    

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# i=0
# sum1=0
# while i<b:
#     a=a*1
#     sum1=sum1+a
#     i=i+1
#     print(a,end=" ")
# print()
# print("sum",sum1)    


# a=int(input("enter the number"))
# s=1
# while a>0:
#     x=a%10
#     num=x*s
#     a=a//10
#     print(num,"+",end=" ")
#     s=s*10

# n=int(input("enter the number"))
# i=1
# sum1=0
# while i<=n:
#     a=(n//10)//10*i
#     print(a)
#     i=i+1


####outpur neha=N_Ee_Hhh_Aaaa
name=input("enter the name")
i=0
while i<len(name): 
    print(name[i].upper()+name[i]*i,end=" ")
    if i!=len(name)-1:
        print("_",end="")
    i=i+1


# def num(a):
#     i=1
#     count=0
#     while i<=a:
#         if a%i==0:
#             print(i)
#             count=count+1
#         i=i+1
#     if count==2:
#         return"prime number"
#     else:
#         return"not prime number"              
# x=int(input("enter the number"))
# print(num(x))    


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#     print(i)