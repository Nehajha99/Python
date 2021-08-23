name=["amisha","srushti","meena","ram"]
age=[20,21,23,24]
work=["softwere engineer","fashion designer","graduation","lawer"]
dic={}
list1=[]
for i in range(len(name)):
    a={"name":name[i],"age":age[i],"work":work[i]}
    dic.update(a)
    list1.append(a)
print(list1)
    
    

