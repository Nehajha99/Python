import json
user=input("Enter whether you wnat to log in or sign up:")
file=open("userdetails.json","r+")
file_name=file.read()
if user=="sign up":
    name=input("Enter your username:")
    password1=input("Enter the password in password  # and @ shoude be present :")
    if "#" or "@" in password1:
        password2=input("confirm the password:")
        if password1==password2:
            print("password is confirmed") 
            dic2={"user":[]}
            b={"name":name,"password":password1}
            if password1 in file_name:
                print("sorry! your name already exist")
            else:
                print("congrets",name,"you are signed up successfully")
                print("now you need to fill the following details")
                description=input("Enter the description:")
                birthdate=input("Enter the birth date:")
                hobbies=input("Enter the hobbies:")
                gender=input("Enter the gender:")
                profil={"description":description,"Birth_date":birthdate,"Hobbies":hobbies,"Gender":gender}
                p="profile"
                b.update({p:profil})
                for i in dic2:
                    ab=dic2[i]
                    ab.append(b)    
            with open("userdetails.json","a") as f:
                json_data=json.dump(dic2,f,indent=2)   
            print("congrats!!",name,"you are signed in succsessfuly")
        else:   
            print("both password not same")


if user=="login":
    username=input("Enter your username:")
    password=input("Enter your password:")
    if password in file_name:
        print("congrats!! "+username+" you are logged in successfully.")
        
    else:
        print("Invalid username and password")












