dic=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
a={}
b=[]
for i in dic:
    p=i
    x=p.values()
    b.append(x)
print(b)
