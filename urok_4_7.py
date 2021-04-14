from math import factorial
n = int(input('Введите значение числа, факториал которого будем искать: '))
def fact(n):
    for i in range(1, n+1):
        yield i
a = fact(n)
print(type(a))
for b in a:
    print(factorial(b))