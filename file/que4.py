f=open("question3.txt","r")
for i in f:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
    else:
        f=open("others.txt","a")
        f.write(i)


