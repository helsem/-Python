from functools import reduce
#проверка
print([el for el in range(100, 1001,2)])
def new_list(c,d):
    return c*d
print(reduce(new_list, [el for el in range(100, 1001,2)]))