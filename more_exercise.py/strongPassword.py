# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule
# follow karne chaiye:
# Kam se kam uski length 6 honi chaiye
# Jada se jada length 16 se jyada na ho
# Kam se kam ek dollar ka sign ($) hona chaiye
# Kam se kam password mein 2 ya 8 hona chaiye
# Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh 
# "Weak Password" type karo

# num=input("enter the password")
# if len(num)>6 and len(num)>16:
#     if "$" in num:
#         if "2" or "8" in num:
#             if "A" or "Z" in num:
#                 print("strong password")
#             else:
#                 print("not")
#         else:
#             print("not")
#     else:
#         print("not")
# else:
#     print("not")                                            


###second way
num=input("enter the password: ")
if (len(num)>6 or len(num)<16) and ("$" in num) and (num>="1" and num<="9" in num) and (num>="a" and  num<="z" in num):
    print("strong password")
else:
    print("not")



                                            