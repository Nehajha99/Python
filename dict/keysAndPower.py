a={}
n=int(input("number of elementes"))
for i in range(1,n):
    k=i**2
    a.update({i:k})
print(a)

