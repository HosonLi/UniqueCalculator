import math
import sys
from decimal import Decimal
import time


def main():
    # load the module of every function
    def uni_variate_function():
        print('\neg. y = kx + b')
        k = Decimal(input('k = '))
        b = Decimal(input('b = '))
        print("This function is 'y =", k, "x +", b, "'.")
        x = Decimal(input('x = '))
        print('y =', (k * x) + b)
        input("Please press 'Enter' to continue.")

    def uni_variate_quadratic_function():
        print('\neg. y = ax*x + bx + c')
        a = Decimal(input('a = '))
        b = Decimal(input('b = '))
        c = Decimal(input('c = '))
        print("This function is 'y =", a, "x*x +", b, "x +", c, "'.")
        x = Decimal(input('x = '))
        print('y =', a * (x * x) + (b * x) + c)
        input("Please press 'Enter' to continue.")

    def inverse_proportional_function():
        print('\neg. y = a / x + b')
        a = Decimal(input('a = '))
        b = Decimal(input('b = '))
        print("This function is 'y =", a, "/ x +", b, "'.")
        x = Decimal(input('x = '))
        print('y =', (a / x) + b)
        input("Please press 'Enter' to continue.")

    def trigonometric_function():
        print('\neg. y = sin(x) / y = cos(x) / y = tan(x) ')
        print('PS: Only radian system is supported.')
        x = Decimal(input('x = '))
        print('y = sin(', x, ') =', math.sin(x))
        print('y = cos(', x, ') =', math.cos(x))
        print('y = tan(', x, ') =', math.tan(x))
        input("Please press 'Enter' to continue.")

    def exponential_function():
        print('\neg. y = a ^ x')
        a = Decimal(input('a = '))
        print("This function is 'y =", a, "^ x'.")
        x = Decimal(input('x = '))
        print('y =', a ** x)
        input("Please press 'Enter' to continue.")

    def logarithmic_function():
        print('\neg. y = ln(x)')
        print('PS: If you want to calculate the logarithm of other bases, please convert it to the logarithm based on '
              'the natural logarithm.')
        x = Decimal(input('x = '))
        print('y =', math.log(x))
        input("Please press 'Enter' to continue.")

    def power_function():
        print('\neg. y = x ^ a')
        a = Decimal(input('a = '))
        print("This function is 'y = x ^", a, "' .")
        x = Decimal(input('x = '))
        print('y =', x ** a)
        input("Please press 'Enter' to continue.")

    # main program
    while True:
        print('\n\nBasic Functions of Middle School Mathematics')
        print('(Only numeric input is supported, otherwise the program will exit automatically.)')
        print("\n----------------------")
        print('1: Uni-variate Function')
        print('2: Uni-variate Quadratic Function')
        print('3: Inverse Proportional Function')
        print('4: Trigonometric Function')
        print('5: Exponential Function')
        print('6: Logarithmic Function')
        print('7: Power Function')
        print('8: Exit Basic Function of Intermediate Mathematical')
        print('9: Exit Calculator')

        choose = input('\nPlease choose pattern:')

        if choose == '1':
            uni_variate_function()
            continue

        elif choose == '2':
            uni_variate_quadratic_function()
            continue

        elif choose == '3':
            inverse_proportional_function()
            continue

        elif choose == '4':
            trigonometric_function()
            continue

        elif choose == '5':
            exponential_function()
            continue

        elif choose == '6':
            logarithmic_function()
            continue

        elif choose == '7':
            power_function()
            continue

        elif choose == '8':
            return

        elif choose == '9':
            print('\nCalculator will exit 2 seconds later!')
            time.sleep(2)
            sys.exit()

        else:
            print('\nPlease input right number!')
            input("Please press 'Enter' to continue.")
            continue
