sub=input("enter the subject:")
dic=[{"math":90,"sci":92},{"math":45,"sci":65},{"math":49,"sci":54}]
i=0
a=[]
while i<len(dic):
    a.append(dic[i][sub])
    i+=1
print(a)
    
