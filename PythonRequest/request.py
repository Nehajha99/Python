import requests
import json
## calling API
saral_data=requests.get("http://saral.navgurukul.org/api/courses")
data=saral_data.json()

#### pushing data in json file
with open("saral_data.json","w") as f:
    json.dump(data,f,indent=4)

##### function for course    
###  this loop for coures name and id   
            
serial_number=1
course_name = data["availableCourses"]
for index_1 in course_name:
    print(serial_number,index_1["name"],":",index_1["id"])
    serial_number+=1
    

#### user input for which course you like to do
user_choose_course=int(input("enter the course number: "))-1
print(course_name[user_choose_course]["name"],course_name[user_choose_course]["id"])

###this link for parents data
parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+course_name[user_choose_course]["id"]+" "+"/exercises")
parents_Data=parents_data.json()
## dump parents data in json file XXXX
with open("parents_data.json","w") as fl:
    json.dump(parents_Data,fl,indent=2)
    

next_previous=input("were you wnats to go next/previous N/P: ").lower() 
if next_previous=="n":
#####parents(child)
    serialNum=1
    child_Data=parents_Data["data"]
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
    In_Courses_next_previous=input("were you wnats to go next/previous N/P: ").lower()
    if next_previous=="n":
        user_choose_course=int(input("enter the course number: "))
        Data=parents_Data["data"][user_choose_course-1]["childExercises"]
        serial_Number=1
        for index_4 in Data:
            print(" ",serial_Number,index_4["name"])
            serial_Number+=1
        #slug
        slugInput=int(input("which question you want to see"))-1
        slugId=Child[slugInput]["id"]
        childSlugName=Child[slugInput]["slug"]            
        slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
        data5=slug_data.json()
        with open("slug_data","w") as File:
            json.dump(data5,File,indent=4)
            print(data5["content"])
    elif  next_previous=="P":
        serialNum=1
        child_Data=parents_Data["data"]
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

# elif next_previous=="p":  
#     saral_data=requests.get("http://saral.navgurukul.org/api/courses")
#     data=saral_data.json()

#     #### pushing data in json file
#     with open("saral_data.json","w") as f:
#         json.dump(data,f,indent=4)

#     ###  this loop for coures name and id   
#     serial_number=1
#     course_name = data["availableCourses"]
#     for index_1 in course_name:
#         print(serial_number,index_1["name"],":",index_1["id"])
#         serial_number+=1

#     #### user input for parents
#     user_choose_course=int(input("enter the course number: "))-1
#     print(course_name[user_choose_course]["name"],course_name[user_choose_course]["id"])

    ###parents data link
    parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+course_name[user_choose_course]["id"]+" "+"/exercises")
    parents_Data=parents_data.json()
    ## dump parents data in json file XXXX
    with open("parents_data.json","w") as fl:
        json.dump(parents_Data,fl,indent=2)   
    next_previous=input("were you wnats to go next/previous N/P: ")    
    if next_previous=="n":
    #####parents(child)
        serialNum=1
        child_Data=parents_Data["data"]
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
        In_Courses_next_previous=input("were you wnats to go next/previous N/P: ")
        if next_previous=="n":
            user_choose_course=int(input("enter the course number: "))
            Data=parents_Data["data"][user_choose_course-1]["childExercises"]
            serial_Number=1
            for index_4 in Data:
                print(" ",serial_Number,index_4["name"])
                serial_Number+=1
            #slug
            slugInput=int(input("which question you want to see"))-1
            slugId=Child[slugInput]["id"]
            childSlugName=Child[slugInput]["slug"]            
            slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
            data5=slug_data.json()
            with open("slug_data","w") as File:
                json.dump(data5,File,indent=4)
                print(data5["content"])

        

                    


# import requests
# import json
# ## calling API

# saral_data=requests.get("http://saral.navgurukul.org/api/courses")
# data=saral_data.json()

# #### pushing data in json file
# with open("saral_data.json","w") as f:
#     json.dump(data,f,indent=4)
# def course():        
# ###  this loop for coures name and id   
#     serial_number=1
#     for index_1 in data["availableCourses"]:
#         print(serial_number,index_1["name"],":",index_1["id"])
#         serial_number+=1
# course()        

# #### user input for which course you like to do
# user_choose_course=int(input("enter the course number: "))-1
# print(data["availableCourses"][user_choose_course]["name"],data["availableCourses"][user_choose_course]["id"])

# ###this link for parents data
# parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data["availableCourses"][user_choose_course]["id"]+" "+"/exercises")
# parents_Data=parents_data.json()
# ## dump parents data in json file XXXX
# with open("parents_data.json","w") as fl:
#     json.dump(parents_Data,fl,indent=2)
    

# next_previous=input("were you wnats to go next/previous N/P: ")    
# if next_previous=="N":
    
# #####parents(child)
#         serialNum=1
#         child_Data=parents_Data["data"]
#         for index_2 in child_Data:
#             print(serialNum,index_2["name"])
#             serialNum+=1
#             if index_2["childExercises"]==[]:
#                 print(" ",index_2["slug"])
#             else:
#                 serialNum2=1 
#                 # Child=index_2["childExercises"]
#                 for index_3 in index_2["childExercises"]:
#                     print("  ",serialNum2,index_3["name"])
#                     serialNum2+=1
#         In_Courses_next_previous=input("were you wnats to go next/previous N/P: ")
#         if In_Courses_next_previous=="N":
#             user_choose_course=int(input("enter the course number: "))
#             Data=parents_Data["data"][user_choose_course-1]["childExercises"]
#             serial_Number=1
#             for index_4 in Data:
#                 print(" ",serial_Number,index_4["name"])
#                 serial_Number+=1
#             #slug
#             slugInput=int(input("which question you want to see"))-1
#             slugId=index_2["childExercises"][slugInput]["id"]
#             childSlugName=index_2["childExercises"][slugInput]["slug"]            
#             slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
#             data5=slug_data.json()
#             with open("slug_data","w") as File:
#                 json.dump(data5,File,indent=4)
#                 print(data5["content"])
#         elif  In_Courses_next_previous=="P":
#             serialNum=1
#             child_Data=parents_Data["data"]
#             for index_2 in child_Data:
#                 print(serialNum,index_2["name"])
#                 serialNum+=1
#                 if index_2["childExercises"]==[]:
#                     print(" ",index_2["slug"])
#                 else:
#                     serialNum2=1 
#                     Child=index_2["childExercises"]
#                     for index_3 in Child:
#                         print("  ",serialNum2,index_3["name"])
#                         serialNum2+=1
    
# elif next_previous=="P":
#     course() 
#     #### user input for which course you like to do
#     user_choose_course=int(input("enter the course number: "))-1
#     print(data["availableCourses"][user_choose_course]["name"],data["availableCourses"][user_choose_course]["id"])

#     ###this link for parents data
#     parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data["availableCourses"][user_choose_course]["id"]+" "+"/exercises")
#     parents_Data=parents_data.json()
#     ## dump parents data in json file XXXX
#     with open("parents_data.json","w") as fl:
#         json.dump(parents_Data,fl,indent=2)
        

#     next_previous=input("were you wnats to go next/previous N/P: ")    
#     if next_previous=="N":
        
#     #####parents(child)
#             serialNum=1
#             child_Data=parents_Data["data"]
#             for index_2 in child_Data:
#                 print(serialNum,index_2["name"])
#                 serialNum+=1
#                 if index_2["childExercises"]==[]:
#                     print(" ",index_2["slug"])
#                 else:
#                     serialNum2=1 
#                     # Child=index_2["childExercises"]
#                     for index_3 in index_2["childExercises"]:
#                         print("  ",serialNum2,index_3["name"])
#                         serialNum2+=1
#             In_Courses_next_previous=input("were you wnats to go next/previous N/P: ")
#             if In_Courses_next_previous=="N":
#                 user_choose_course=int(input("enter the course number: "))
#                 Data=parents_Data["data"][user_choose_course-1]["childExercises"]
#                 serial_Number=1
#                 for index_4 in Data:
#                     print(" ",serial_Number,index_4["name"])
#                     serial_Number+=1
#                 #slug
#                 slugInput=int(input("which question you want to see"))-1
#                 slugId=index_2["childExercises"][slugInput]["id"]
#                 childSlugName=index_2["childExercises"][slugInput]["slug"]            
#                 slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
#                 data5=slug_data.json()
#                 with open("slug_data","w") as File:
#                     json.dump(data5,File,indent=4)
#                     print(data5["content"])
#             elif  In_Courses_next_previous=="P":
#                 serialNum=1
#                 child_Data=parents_Data["data"]
#                 for index_2 in child_Data:
#                     print(serialNum,index_2["name"])
#                     serialNum+=1
#                     if index_2["childExercises"]==[]:
#                         print(" ",index_2["slug"])
#                     else:
#                         serialNum2=1 
#                         Child=index_2["childExercises"]
#                         for index_3 in Child:
#                             print("  ",serialNum2,index_3["name"])
#                             serialNum2+=1 
        














