# Que-Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. Ek aisa code likho jisse
# aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. Jaise:
 
s= ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish","neha"]
i=0
a=[]
while i<len(s):
    j=0
    while j<len(s):
        if s[i]==s[j] not in a:
            a.append(s[j])
        j=j+1
    i=i+1
print(a)            
    
