# Ek code likhiye jo dictionary ki 3 highest value print karaye. Example :-
my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100, 'f':20}
a=[]
b=[]
for i in range(3):
    max_1=0
    for value in my_dict:
        if max_1<my_dict[value]:
            max_1=my_dict[value]
            key=value
    a.append(max_1)
    b.append(key)
    my_dict.pop(key)
print(a)
print(b)
# 
# my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100, 'f':20}
# #a=[]
# b=[]
# a={}
# for i in my_dict:
#         x=my_dict[i]
#         y=i
#         b.append((x,y))
# a.update(b)
# print(a)
# y=list(a)
# n=y
# a=[]
# max1=n[0]
# for i in n:
#     if max1<i:
#         max1=i
# first_max=max1
# a.append(first_max)
# y.remove(max1)
# max2=n[0]
# for i in n:
#     if max2<i:
#         max2=i
# s_max=max2
# a.append(s_max)
# y.remove(max2)
# max3=n[0]
# for i in n:
#     if max3<i:
#         max3=i
# t_max=max3
# a.append(t_max)
# print(a)
            

        






    







