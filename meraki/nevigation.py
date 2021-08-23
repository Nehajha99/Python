import requests
import json
## calling API
saral_data=requests.get("http://saral.navgurukul.org/api/courses")
data=saral_data.json()

#### pushing data in json file
with open("saral_data.json","w") as f:
    json.dump(data,f,indent=4)
    ###  this loop for coures name and id

serial_number=1
course_name = data["availableCourses"]
for index_1 in course_name:
    print(serial_number,index_1["name"],":",index_1["id"])
    serial_number+=1        
#### user input for which course you like to do
user_choose_course=int(input("enter the course number: "))-1
id=course_name[user_choose_course]["id"]
print(course_name[user_choose_course]["name"])    

user=input("do you wants to go with this course YES/NO: ").lower()
if user=="yes":
    ### course id
    courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
    courseID_data=courseID.json()
    ####pushing id in json
    with open("courseID.json","w") as fh:
        json.dump(courseID_data,fh,indent=4)
    ###course name
    serial_number2=1 
    for i in courseID_data:
        print(i)
        for j in courseID_data[i]:
            print(serial_number2,j["name"])
            serial_number2+=1
###################################################        
next_previous1=input("do you wants to go with this course YES/NO: ").lower()
if next_previous1=="no":
    saral_data=requests.get("http://saral.navgurukul.org/api/courses")
    data=saral_data.json()

    #### pushing data in json file
    with open("saral_data.json","w") as f:
        json.dump(data,f,indent=4)

    ###  this loop for coures name and id   
    serial_number=1
    course_name = data["availableCourses"]
    for index_1 in course_name:
        print(serial_number,index_1["name"],":",index_1["id"])
        serial_number+=1

    #### user input for which course you like to do
    user_choose_course=int(input("enter the course number: "))-1
    id=course_name[user_choose_course]["id"]

    #### course id
    courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
    courseID_data=courseID.json()###course name
    

    ####pushing id in json
    with open("courseID.json","w") as fh:
        json.dump(courseID_data,fh,indent=4)
    ###course name
    serial_number2=1 
    for i in courseID_data:
        for j in courseID_data[i]:
            print(serial_number2,j["name"])
            serial_number2+=1            
       
#####child
child=int(input("enter the child number"))
serialNum=1
for i in courseID_data:
    a=courseID_data[i][child-1]["childExercises"]
    serialNum=1
    for j in a:
        print("**",serialNum,j["name"])
        serialNum+=1

    slugInput=int(input("which question you want to see"))-1
    slugId=a[slugInput]["id"]
    childSlugName=a[slugInput]["slug"]            
    slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+slugId+"/exercise/getBySlug?slug="+str(childSlugName))
    data5=slug_data.json()
    with open("slug_data.json","w") as File:
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

# ###  this loop for coures name and id   
# serial_number=1
# course_name = data["availableCourses"]
# for index_1 in course_name:
#     print(serial_number,index_1["name"],":",index_1["id"])
#     serial_number+=1

# #### user input for which course you like to do
# user_choose_course=int(input("enter the course number: "))-1

# #### course id
# courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
# courseID_data=courseID.json()

# ####pushing id in json
# with open("courseID.json","w") as fh:
#     json.dump(courseID_data,fh,indent=4)


# ##course name
# serial_number2=1 
# for i in courseID_data:
#     for j in courseID_data[i]:
#         print(serial_number2,j["name"])
#         serial_number2+=1
# ###################################################        
# next_previous1=input("werw you wants to go NEXT/PREVIOUS (n/p)")
# if next_previous1=="p":
#     saral_data=requests.get("http://saral.navgurukul.org/api/courses")
#     data=saral_data.json()

#     #### pushing data in json file
#     # with open("saral_data.json","w") as f:
#     #     json.dump(data,f,indent=4)

#     ###  this loop for coures name and id   
#     serial_number=1
#     course_name = data["availableCourses"]
#     for index_1 in course_name:
#         print(serial_number,index_1["name"],":",index_1["id"])
#         serial_number+=1

#     #### user input for which course you like to do
#     user_choose_course=int(input("enter the course number: "))-1
#     id=course_name[user_choose_course]["id"]

#     #### course id
#     courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
#     courseID_data=courseID.json()###course name
    

#     ####pushing id in json
#     with open("courseID.json","w") as fh:
#         json.dump(courseID_data,fh,indent=4)
#     ###course name
#     serial_number2=1 
#     for i in courseID_data:
#         for j in courseID_data[i]:
#             print(serial_number2,j["name"])
#             serial_number2+=1            
# courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
# courseID_data=courseID.json()###course name
    

#     ####pushing id in json
# with open("courseID.json","w") as fh:
#     json.dump(courseID_data,fh,indent=4)
# ###course name
# serial_number2=1 
# for i in courseID_data:
#     for j in courseID_data[i]:
#         print(serial_number2,j["name"])
#         serial_number2+=1              
# #####child
# child=int(input("enter the child number"))
# serialNum=1
# for i in courseID_data:
#     a=courseID_data[i][child-1]["childExercises"]
#     serialNum=1
#     for j in a:
#         print("**",serialNum,j["name"])
#         serialNum+=1 




