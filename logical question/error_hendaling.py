# list1=["123s","874w","675","890","789r"]
# new_list=[]
# for i in range(len(list1)):
#     try:
#         b=int(list1[i])
#         new_list.append(b)
#     except Exception:
#         pass
# print(new_list)    

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f"{person}'s age is unknown.")

