import re

print('''Simple Python Calc

Supports addition, subtraction, division,
multiplication, modulo, and powers.

Future updates will hopefully include actual equations and such!

''')
def calc():

    user_string = input("Input your equation: ")
    user_string = user_string.split(' ')
    x, y = user_string[0], user_string[-1]
    ans = 0


    if len(user_string) != 3:
        print("invalid input, try again")
        exit()

    op = user_string[1]
    if '+-*/^%' in op:

        if op == '+':
            ans = x + y
        elif op == '-':
            ans = x - y
        elif op == '*':
            ans = x * y
        elif op == '/':
            ans = x / y
        elif op == '^':
            ans = x ** y
        elif op == '%':
            ans = x % y

        return ans

print(calc())