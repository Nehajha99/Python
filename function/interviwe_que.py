# a="[{([])}]"
# c=list(a)
# print(c)
# b=[]
# i=0
# count=0
# while i<len(c) and i<=len(c)/2:
#     print(c[i])
#     print(c[-i])
#     #if x==y:
#        # count=count+1
#     i=i+1
#     #print(count,x,y)        
# a="[{([])}]"
# c=list(a)
# print(c)
# i=0
# count=0
# while i<len(c)/2:
#     x=a[i]
#     print(x)
#     j=0
#     while j<=len(c[i])/2:
#         y=c[-i]
#         print(y)
#         j=j+1
#     i=i+1
# 
ch = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11,10] 
ch1=[]
i=0
while i<len(ch):
    j=0
    count=0
    a = []
    while j<len(ch):
        if ch[i]==ch[j]:
            count=count+1
        j=j+1
    a.append(ch[i])
    a.append(count//2)   
    if a not in ch1:
        ch1.append(a)    
    i=i+1
print(ch1)  