"""Calculator V1."""
print(
    "Hi, this calculator works based on the command 'EVAL'\n"
    "it works in an infinite loop, if you need to end it, write \n'"
    "1/0 or another mathematical combination that will cause an error,"
    " also if you pass a letter (string) you can also exit the program'")
while True:
    try:
        print(f'solution = {eval(input("Enter an expression to calculate in the format 1 + 1: "))}')
    except (ZeroDivisionError, NameError) as error:
        print('Calculator end work')
# pylint calculator_v1.py - 8.33/10 W0123: Use of eval (eval-used)
