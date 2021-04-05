second = int(input('Введите количество секунд: '))
hour = second // 3600
rest = second % 3600
minutes = rest // 60
second_2 = rest % 60
print(hour, minutes,second_2)
print("{:02d} : {:02d} : {:02d}".format(hour, minutes, second_2))
