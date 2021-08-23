def check_numbers(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i] and b[j] %2==0:
            print("evan number",a[i],b[j])
        else:
            print("odd number",a[i],b[j])
        i=i+1
        j=j+1
x=[2, 6, 18, 10, 3, 75]
y=[6, 19, 24, 12, 3, 87]
check_numbers(x,y)