#### enumerater give us index and item both
a= [1, -2, -3, 4, -5, 1, -2, -3, 4, 5, -1]
for n, i in enumerate(a):
      if i<0:
            a[n] = 0
print(a)
