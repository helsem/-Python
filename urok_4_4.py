my_list =[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
print([my_list[num] for num in range(0, len(my_list)-1) if int(my_list[num])!=int(my_list[num+1])])