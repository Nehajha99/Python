# import requests
# import json

# saral_data=requests.get("http://saral.navgurukul.org/api/courses")
# data=saral_data.json()

# #### send data in json file
# with open("saral_data.json","w") as f:
#     json.dump(data,f,indent=4)

# ###  this loop for coures name and id   
# serial_number=1
# course_name = data["availableCourses"]
# for index_1 in course_name:
#     print(serial_number,index_1["name"],":",index_1["id"])
#     serial_number+=1

# #### user input for parents
# user_choose_course=int(input("enter the course number: "))-1
# print(course_name[user_choose_course]["name"],course_name[user_choose_course]["id"])

# ###parents data link
# parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+course_name[user_choose_course]["id"]+" "+"/exercises")
# parents_Data=parents_data.json()
# ## dump parents data in json file XXXX
# with open("parents_data.json","w") as fl:
#     json.dump(parents_Data,fl,indent=2)

# #####parents(child)
# serialNum=1
# child_Data=parents_Data["data"]
# for index_2 in child_Data:
#     print(serialNum,index_2["name"])
#     serialNum+=1
#     if index_2["childExercises"]==[]:
#         print(" ",index_2["slug"])
#     else:
#        s_num2=1 
#        Child=index_2["childExercises"]
#        for index_3 in Child:
#            print("  ",s_num2,index_3["name"])
#            s_num2+=1
# next_previous=input("were you wnats to go next/previous N/P: ")
# if next_previous=="N":
#     continue_course=input("do you want to continue with this course y/n: ")
#     if continue_course=="n": 
#         serial_no=1
#         courses_name = data["availableCourses"]
#         for index_1 in courses_name:
#             print(serial_no,index_1["name"],":",index_1["id"])
#             serial_no+=1
#             user_choose_course=int(input("enter the course number: "))-1
#             print(courses_name[user_choose_course]["name"],courses_name[user_choose_course]["id"])
#             s_num=1
#             child_Data=parents_Data["data"]
#             for index_2 in child_Data:
#                 print(s_num,index_2["name"])
#                 s_num+=1
#                 if index_2["childExercises"]==[]:
#                     print(" ",index_2["slug"])
#                 else:
#                     s_num2=1 
#                     Child=index_2["childExercises"]
#                     for index_3 in Child:
#                         print("  ",s_num2,index_3["name"])
#                         s_num2+=1
#                 course_name=int(input("Enter in which topic you wants to go: "))
#                 Data=parents_Data["data"][course_name-1]["childExercises"]
#                 for index_4 in Data:
#                     print(index_4["name"])
#     continue_course=="y"
#     course_name=int(input("Enter in which topic you wants to go: "))
#     Data=parents_Data["data"][course_name-1]["childExercises"]
#     print(Data)
#     for index_4 in Data:
#         print(index_4["name"])
            
# ##slug
# slugInput=int(input("which question you want to see"))
# print(course_name[user_choose_course]["name"],course_name[user_choose_course]["id"])
# print(Data[slugInput]["name"],Data[slugInput]["id"])            
# slug_data=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json" )
# data5=slug_data
# #####dump parant dic
# with open("slug_data","w") as File:
#     json.dump(data5,File,indent=4)
# print(data5)