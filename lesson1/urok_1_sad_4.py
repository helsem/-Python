n = input('Введите положительное число: ')
while int(n) > 0:
    i = 0
    maxi = 0
    b = len(n)
    for i in range(0, b):
        if int(n[i]) > maxi:
            maxi = int(n[i])
        i += 1
    print('Самая большая цифра в числе ', n, ' - ', maxi)
    break
if int(n) < 0:
    print('Напоминаю, у положительных чисел отсутствует знак "-"')
elif int(n) == 0:
    print('Напоминаю, у нуля нет знака')