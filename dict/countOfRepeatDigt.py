 
# a="MISSISSIPPI" 
# p=(list(a))
# ch=[]
# i=0
# while i<len(p):
#     j=0
#     count=0
#     a1=[]
#     while j<len(p):
#         if p[i]==p[j]:
#             count=count+1
#         j=j+1
#     a1.append(p[i])
#     a1.append(count)
#     if a1 not in ch:
#         ch.append(a1)
#     i=i+1        
# print(ch)  


#####second way
# a="MISSISSIPPI" 
# p=list(a)
# dic={}
# for j in p:
#     a=p.count(j)
#     dic.update({j:a})
# print(dic)























# b = []
# a=[1,2,3,4,5,6,7,8]
# a1=int(input("enter the number"))
# i=1
# while i<=a1:
#     b.append(a[i-1])
#     #b.append(a[-i])
#     i+=1
#     b.append(a[-i])    
# print(b)




















# a=[1,2,3,4,5,6,7,8]
# a1=int(input("enter the number"))
# j=0
# i=1
# x1=[]
# while i<len(a):
#     if i<=a1:
#         x=a[-i]
#     if j<(len(a-a1)):
#         y=a[j]
#     i=i+1
#     x1.append(y)
#     x1.append(x)
# print(x1)    

    