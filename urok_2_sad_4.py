n = input('Введите предложение: ')
for i in range (0, len(n.split())):
    print(i+1, ')', n.split()[i][0:10])



