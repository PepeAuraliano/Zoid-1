# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def div (arg1, arg2):
    try:

      res = arg1 / arg2
    except ValueError:
       return "Ошибка значения"
    except ZeroDivisionError:
        return "Неправилтьный делитель, вы не можете использовать ноль как делитель"
    return res

one = int(input("Ведите делимое "))
two = int(input("Ведите делитель "))
res = one / two
div(one, two)
print(div(arg1=one, arg2=two),type(res))