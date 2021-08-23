keys=["name","designation","age","salary"]
value1=["neelam","programer","24","2400",]
a={}
b={}
c={}
d={}
new_dic={}
for i in range(len(keys)):
    a[keys[i]]=value1[i]
    new_dic["emp1"]=a

value2=["komal","trainer","24","20000"]
for i in range(len(keys)):
    b[keys[i]]=value2[i]
    new_dic["emp2"]=b
value3=["anuradha","HR","25","40000"]
for i in range(len(keys)):
    c[keys[i]]=value3[i]
    new_dic["emp3"]=c

value4=["Abhishek","manager","29","63000"]
for i in range(len(keys)):
    d[keys[i]]=value4[i]
    new_dic["emp4"]=d
import json
with open("que8.json","w") as f:
    a=json.dump(new_dic,f,indent=1)    

