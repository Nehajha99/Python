a={"object":
[
    {"soap":"lux","name":1222},
    {"top":"null","name":225},
    {"pop":"null","name":8736},
    {"education":"pass","name":328}
    ]
}
p=[]
for i in a.values():
    for j in i:
        for m in j.values():
            p.append(m)
list1=p
new_list=[]
for x in list1:
    if type(x)==int:
        new_list.append(x)
print(new_list)

### find min max panding


