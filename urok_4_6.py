from itertools import count, cycle
a = int(input('Введите начало: '))
b = int(input('Введите конец: '))
for el in count(a):
    if el>b:
        break
    else:
        print(el)
c = int(input('Введите количество повторов: '))
d = 0
for el in cycle(input('Введите список, который будете повторять: ')):
    if d>c:
        break
    else:
        print(el)
        d+=1