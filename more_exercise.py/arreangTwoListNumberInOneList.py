# Que--Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements hone
# chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone
# chaiye. Agar humare paas yeh do lists hain:
 
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
#print(list2)
# is ma hum sorted use kare gye question ke jese output ke liye.
print(sorted(list2))    

