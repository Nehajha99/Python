#### que-Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki niche dikhaya
#gaya hai (Sample Data) aur uske baad saare unique values ko ek list me print karaye. 
dic=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
new_list=[]
for i in dic:
    for a in i:
        p=(i[a])
        if p not in new_list:
            new_list.append(p)
print(new_list)  



        

