# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# } 

#### json to python
# import json
# j='{"name":"neha","city":"delhi","year":2020}'
# p=json.loads(j)
# print(p)
# print(type(p))


#### python to json
#import json
# j={"name":"neha","city":"delhi","year":2020}
# p=json.dumps(j)
# print(p)
# print(type(p))

# age=20
# p=json.dumps(age)
# print(type(p))    
#### json m number sring ho jata h kya


####white space
### in json indent give us white space.
# import json
# city=("indore","burhanpur","dhar")
# print(json.dumps(city))
# print(json.dumps(city,indent=44))



### separators 
# import json
# city=("indore","burhanpur","dhar")
# print(json.dumps(city))
# print(json.dumps(city,separators=(",",".")))

