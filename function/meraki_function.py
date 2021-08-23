# print ("NavGurukul")

# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")

# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello() 

# def definition_say_hello():
#     print ("NavGurukul")
#     print ("NavGurukul mei humein apni learning ki responsibility leni padti hai.")

# definition_say_hello()

# print ("NavGurukul mei hum sab logo ko ek tarah se treat karte hai.")

# definition_say_hello() 

# def definition_hello_again():
#     print ("Firse Hello :)")
#     print ("Aap kaise ho?") 
# definition_hello_again()

#function arguments
#withount arguments
# def addition():
#     a=int(input("enter 1st number"))
#     b=int(input("enter 2ed number"))
#     c=a+b
#     print("addition=",c)
# addition()    

# with arguments
# def addition(a,b):
#     c=a+b
#     print("addition=",c)
# #addition(2,9)
# a=int(input("enter your 1st number"))
# b=int(input("enter your 2ed number"))
# addition(a,b)

#even odd with arguments
# def even():
#     a=int(input("enter the number"))
#     if a%2==0:
#         print("evan=",a)
#     else:
#         print("odd=",a)    
# even()            

#even odd with arguments
# def even_odd(a):
#     if a%2==0:
#         print("evan=",a)
#     else:
#         print("odd=",a)
# x=int(input("enter the number"))
# even_odd(x)            

###return statement
# def add(a,b):
#     c=a+b
#     return(c)
# a=int(input("enter 1st number"))
# b=int(input("enter 2ed number"))
# z=add(a,b)
# print("addition=",z) 

#max with return
# def mix(a):
#     mix=a[0]
#     i=0
#     while i<len(a):
#         if mix<a[i]:
#             mix=a[i]
#         i=i+1
#     return (mix)
# a = [50, 40, 23, 70, 56, 120,6, 5, 10, 7,]
# print(mix(a))
# mix without return
# def mix(a):
#     mix=a[0]
#     i=0
#     while i<len(a):
#         if mix<a[i]:
#             mix=a[i]
#         i=i+1
#     print(mix)
# mix([50, 40, 23, 70, 56, 120,6, 5, 10, 7,])


###minimum
# def m(a): 
#     m=a[0]
#     i=0
#     while i<len(a):
#         if m>a[i]:
#             m=a[i]
#         i=i+1
#     print(m)
# m([1, 2, 3, 4, 5])

# def m(a): 
#     m=a[0]
#     i=0
#     while i<len(a):
#         if m>a[i]:
#             m=a[i]
#         i=i+1
#     return(m)
# a=[1, 2, 3, 4, 5]
# print(m(a))
# 
####
# def r(a):
#     i=1
#     c=[]
#     while i<=len(a): 
#         n=(a[-i])
#         c.append(n)
#         i=i+1
#     return c
# s=r(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])
# print(s)

# numbers = [1, 2, 3, 4, 5]
# def s(numbers):
#     i=0
#     add=0
#     while i<len(numbers):
#         add=add+numbers[i]
#         i=i+1
#     return add 
# n=s([1, 2, 3, 4, 5])
# print(n)

# def sum():
#     print(12+13)
# sum()
         
# def welcome():
#     print("Welcome to function")
# welcome()             


# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()         

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")         
# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name) 
#def icecream(*flavours):
#     for i in flavours:
#         print("i love",i)

# icecream("chocolate", "butterscotch","vanilla","strawberry") 
# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif") 

# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif") 

# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh") 
# def greet(*names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 
# def info(name, age ="23" ):
#        print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")
# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","neha")  
#QUESTION-2
# "Mera naam Rishabh hai." aur "Main NavGurukul ka co-Founder hun." print karao.
# def function(name,masti):
#     print(name,"aur",masti)
# function("mera naam neha hai","main navgurukul ki ceo hun")    
# def students(a):
#     for i in range(0,len(a)):
#         print(a[i])
# list_of_student=["amisha","neha"]
# students(list_of_student)  


####question 2
# def is_greater_20(a,b=20):
#     if a>b:
#         print("a is greater")
#     else:
#         print("b is greater")

# a=3
# is_greater_20(a)


#####question4
# def add_number(num1,num2):
#     num3=num1+num2
#     print("add=",num3)
# num1=56
# num2=12
# add_number(num1,num2)    
# def add_number(num1,num2):
#     i=0
#     j=0
#     while i<len(num1) and j<len(num2):
#         num3=num1[i]+num2[j]
#         print("add=",num3)
#         j=j+1
#         i=i+1 
# a=[50,60,10]
# b=[10,20,13]
# add_number(a,b)

####question5
# def check_numbers(a,b):
#     i=0
#     j=0
#     while i<len(a) and j<len(b):
#         if a[i] and b[j] %2==0:
#             print("evan number",a[i],b[j])
#         else:
#             print("odd number",a[i],b[j])
#         i=i+1
#         j=j+1
# x=[2, 6, 18, 10, 3, 75]
# y=[6, 19, 24, 12, 3, 87]
# check_numbers(x,y)

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# number_a = add_numbers(20, 40) ** add_numbers(5, 1)
# print (number_a)     

###question7
# def age_of_vote(age):
#     if age>=18:
#         print("eligible for vote")
#     else:
#         print("not eligible")
# num=int(input("enter the age"))
# age_of_vote(num)            


# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function() 

# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    

# first_function()  

# def age_of_vote(age):
#     if age>=18:
#         return "eligible for vote"
#     else:
#         return "not eligible"
# num=int(input("enter the age"))
# vote=age_of_vote(num)
# print(vote)

###que2
# a=int(input("enter the number"))
# def per(a):
#     i=1
#     mul=1
#     while i<a:
#         if a%i==0:
#             mul=mul*i
#         i=i+1
#     #print(mul)
#     if mul==a:
#         print("perfect number")
#     else:
#         print("not perfect number")
# x=int(input("enter the number"))
# per(x)    


####que3
# def amisha(a,b,c):
#     x=a+b+c
#     a=x/3
#     print(x)
#     print(a)
# x=int(input("enter the number"))
# y=int(input("enter the number"))
# z=int(input("enter the number"))
# amisha(x,y,z)
 
# ####que4
# def evan(a):
#     i=0
#     while i<=a:
#         if i%2==0:
#             print("evan number=",i)
#         else:
#             print("odd number=",i)
#         i=i+1
# num=int(input("enter the number"))    
# evan(num)                 

####que5
# def mom(x):
#     i=1
#     sum=0
#     while i<=x:
#         if i%3==0:
#             print(i)
#             sum=sum+i
#         if i%5==0:
#             print(i)
#             sum=sum+i
#         i=i+1
#     print(sum) 
# x=int(input("enter the number"))
# mom(x)

# def mom(a):
#     i=1
#     s=0
#     while i<=a:
#         if i%3==0 or i%5==0:
#             print(i)
#             s=s+i
#         i=i+1
#     print(s)    
# x=int(input("enter the number"))
# mom(x)
####que7
# def sajan(a,b):
#     if len(a)<len(b):
#         print(b)
#     elif len(a)>len(b):
#         print(a)
#     elif len(a)==len(b):
#         print(a,b)    
# x=input("enter the name")
# y=input("enter the name")
# sajan(x,y)
 
####que8
# def squre(a):
#     i=0
#     while i<=a:
#         print(i,":",i**2)
#         i=i+1
# x=int(input("enter the number"))
# squre(x)        

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# s=sumofdigits(123)
# print(s)
 
                             