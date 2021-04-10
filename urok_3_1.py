def calc_division (divisible, divisor):
    try:
        return(divisible/divisor)
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'
print(calc_division(int(input(f'введите делимое ')),int(input(f'введите делитель  '))))