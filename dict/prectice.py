# list1=["one","two","three","four","five"] 
# a = {}
# a["1"]=list1[0]
# a["2"]=list1[1]
# a["3"]=list1[2]
# a["4"]=list1[3]
# a["5"]=list1[4]
# print(a)


#####list to dic
# a=[("name","prity"),("gender","female")]
# dic={}
# dic.update(a)
# print(dic)


#####dic to list
# a=[]
# b=[]
# dic={"name":"prity","sex":"female"}
# for i in dic.keys():
#     a.append(i)
# print(a)

####prime number
# i=1
# while i<=100:
#     j=1
#     count=0
#     while j<=100:
#         if i%j==0:
#             count=count+1
#         j=j+1    
#     if count==2:
#         print(i,"prime number")
#     else:
#         print(i,"not prime number")
#     i=i+1        
        
            
# name=["amisha","srushti","meena","ram"]
# age=[20,21,23,24]
# work=["softwere engineer","fashion designer","graduation","lawer"]#it working for even number list like 2 list or 4list
# n=zip(name,age)
# list1=list(n)
# dict1=dict(list1)
# print(dict1)

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit) 


# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box])) 
#### find the error


# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1
# print(sum) 

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)  

####### que 1
# dic=[{"name":"golmal","language":"hindi","release year":2016},
# {"name":"kissing both","language":"hindi","release year":2015},
# {"name":"arjun reddy","language":"hindi","release year":2012},
# {"name":"bindass","language":"hindi","realise date":2000},
# {"name":"challenge","language":"hindi","realise date":1998},
# {"name":"yuddho","language":"hindi","realise date":1999},
# {"name":"kabir singh","language":"hindi","realise date":2020},
# {"name":"angreji medium","language":"hindi","realise date":2020},
# {"name":"thappad","language":"hindi","realise date":2019},
# {"name":"avenger","language":"english","realise date":2018},
# {"name":"forest Gump","language":"english","realise date":2017},
# {"name":"Roohi","language":"tamil","realise date":2005},
# {"name":"bangalore days","language":"malyalam","realise date":2008}]
# list2=[]
# for i in dic:
#     p=i["language"]
#     list2.append(p)
# list1=list2
# i=0
# a=[]
# b=[]
# while i<len(list1):
#     count=0
#     m=list1[i]
#     j=0
#     while j<len(list1):
#         n=list1[j]
#         if m==n:
#             b.append(n)
#             count=count+1
#         j=j+1
#     k=0
#     while k<len(list1):
#         if m not in a:
#             a.append(m)
#             print(m,count)
#         k=k+1
#     i=i+1                



###que 2
# a="VTU12.e-Learning"
# letter,digit,lower,upper=0,0,0,0
# for i in a:
#     if i.isalpha():
#         letter=letter+1
#     if i.isdigit():
#         digit=digit+1
#     if i.islower():
#         lower=lower+1
#     if i.isupper():
#         upper=upper+1
# print(letter)
# print(digit)
# print(upper)
# print(lower)                    


# a='The quick Brow Fox'
# lower=0
# upper=0
# for i in a:
#     if i>="A" and i<="Z":
#         upper=upper+1
#     elif i>="a" and i<="z":
#         lower=lower+1   
# print("upper",upper)
# print("lower",lower)        


























