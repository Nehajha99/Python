i=1
while i<=100:
    if i%3==0:
        print("nav")
    if i%7==0:
        print("gurukul")
    if i%3==0 and i%7==0:
        print("navgurukul")
    else:
        print(i)    
    i=i+1 