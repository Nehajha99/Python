dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
 

list1=[]
count=0
for i in dict1:
    for j in dict1[i]:
        count=count+1
print(count)        
    


