"""Calculator V2, very easy calculator."""
first_arg, second_arg = int(input("Первое число: ")), int(input("Второе число: "))
operations = int(input("Второе число: ")), input("Операция с этими числами(Доступны: + - * /) :")
if operations not in '+-*/':
    print("операция недоступна")
else:
    if operations == '+':
        print(f'{first_arg} {operations} {second_arg} = {first_arg + second_arg}')
    elif operations == '-':
        print(f'{first_arg} {operations} {second_arg} = {first_arg + second_arg}')
    elif operations == '*':
        print(f'{first_arg} {operations} {second_arg} = {first_arg * second_arg}')
    else:
        if second_arg == 0:
            print('Деление на 0, серьёзно?')
        else:
            print(f'{first_arg} {operations} {second_arg} = {first_arg / second_arg}')

# pylint calculator_v2.py - 10/10
