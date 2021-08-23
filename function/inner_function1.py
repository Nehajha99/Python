def age_of_vote(age):
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible")
num=int(input("enter the age"))
age_of_vote(num)    