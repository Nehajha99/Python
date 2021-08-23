a = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]  
i=0
p=[]
while i<len(a):
    j=0
    max1=a[i][j]    
    while j<len(a[i]):
        if max1<a[i][j]:
            max1=a[i][j]
            p.append(max1)
        j=j+1    
    i=i+1
    #print(max1)
print(p)