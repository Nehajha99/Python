import requests
import json
## calling API
saral_data=requests.get("http://saral.navgurukul.org/api/courses")
data=saral_data.json()
#### pushing data in json file
with open("saral_data.json","w") as f:
    json.dump(data,f,indent=4)

def meraki_course():          
    ###  this loop for coures name and id   
    serial_number=1
    for index_1 in data["availableCourses"]:
        print(serial_number,index_1["name"],":",index_1["id"])
        serial_number+=1
meraki_course()        
            
#### user input for which course you like to do
user_choose_course=int(input("enter the course number: "))-1
print(data["availableCourses"][user_choose_course]["name"])
user=input("do you want to previous ").lower()
if user=="p":
    meraki_course()
###this link for parents data
parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data["availableCourses"][user_choose_course-1]["id"]+" "+"/exercises")
parents_Data1=parents_data.json()
## dump parents data in json file XXXX
with open("parents_data.json","w") as fl:
    json.dump(parents_Data1,fl,indent=2)

def saral_data():    
#####parents(child)
    serialNum=1
    print("slu",parents_Data1["data"][1]["slug"])
    child_Data=parents_Data1["data"]
    for index_2 in child_Data:
        print(serialNum,index_2["name"])
        serialNum+=1
        if index_2["childExercises"]==[]:
            print(" ",index_2["slug"])
        else:
            serialNum2=1 
            Child=index_2["childExercises"]
            for index_3 in Child:
                print("  ",serialNum2,index_3["name"])
                serialNum2+=1













# saral_data()
# slug=int(input("enter the number of parents:"))
# print(parents_Data1["data"][slug-1]["name"])

# user_choose_course=int(input("enter the course number: "))-1
# print(data["availableCourses"][user_choose_course]["name"])
# Number1=input("do you want to previous or next").lower()
# if Number1=="p":
#     print(" ")

# saral_data()

# slug_content=[]
# no=0
# list=[]
# for child in range(len(parents_Data1["data"])):
#     no=+1
#     serial_no=1
#     if parents_Data1["data"][child]["childExercises"]==list:
#         serial_no += 1

#         Serial_Number=1
#         for Question in range(len(parents_Data1["data"][slug-1]["childExercises"])):
#             if parents_Data1["data"][child]["childExercises"] == list:
#                 print("      ",Serial_Number,".",parents_Data1["data"][slug-1]["chilExercises"][Question]["name"])
#                 slug1 = parents_Data1["data"][slug-1]["chilExercises"][Question]["slug"]
#                 parent = parents_Data1["data"][slug-1]["chilExercises"][Question]["id"]
#                 slug2 = requests.get("http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug)

#                 slug3 = slug2.json()
#                 slug_content.append(slug3["content"])
#                 Serial_Number += 1

    
# user_choose_course=int(input("enter the course number: "))
# Data=parents_Data["data"][user_choose_course-1]["childExercises"]
# serial_Number=1
# for index_4 in Data:
#     print(" ",serial_Number,index_4["name"])
#     serial_Number+=1
# slug
# slugInput=int(input("which question you want to see"))-1
# slugId=Child[slugInput]["id"]
# childSlugName=Child[slugInput]["slug"]            
# slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
# data5=slug_data.json()
# with open("slug_data","w") as File:
#     json.dump(data5,File,indent=4)
#     print(data5["content"])

