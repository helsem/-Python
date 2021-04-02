n = int(input('Введите количество элементов, из которых будет состоять список: '))
a = []
i = 0
for i in range(0, n):
    a.append(input('Введите элемент списка: '))
    print(i+1, '- ый: ', a[i])
    i += 1
b = a.copy()
i = 0
while n>=1:
    for i in range(0, n-1, 2):
        a[i] = b[i+1]
        a[i+1] = b[i]
    print(a)
    break
if n<1:
    print('такого количества элементов задача не предусматривает')



