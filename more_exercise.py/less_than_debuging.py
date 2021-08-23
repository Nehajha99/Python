def numbers_less_than_twenty(list1):
    counter = 0
    while counter < len(list1):
        item = list1[counter]
        if item < 20:
            list1.remove(item)
        else:
          counter += 1
    return list1

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

s=num_list_sub_20 = numbers_less_than_twenty(num_list)
# print(s)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)