# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

def sal():
    try:
        time = float(input('Выработка в часах '))
        rate = int(input('Ставка в рублях '))
        bonus = int(input('Премия в рублях '))
        res = time * rate + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Это не число4')
sal()