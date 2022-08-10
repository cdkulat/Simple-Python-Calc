import pyinputplus as inp
import re

print('''Simple Python Calc

Supports addition, subtraction, division,
multiplication, modulo, and powers.

Future updates will hopefully include actual equations and such!

''')

print("Currently only supports equations with two values and one operator.")
user_string = input("Input your equation: ")

user_string = user_string.split(' ')

if len(user_string) != 3:
    print("invalid input, try again")
    exit()

op = user
if user_string[1] == '=-*/':
    if user_string
