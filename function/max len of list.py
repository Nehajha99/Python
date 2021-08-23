a=[[1,2],[4,7,8],[8,6,3,2],[5,6,7,1,3],[1]]
i=0
s=len(a[i])
while i<len(a):
    if s<len(a[i]):
        s=len(a[i])
        b=a[i]
    i+=1
print(b)