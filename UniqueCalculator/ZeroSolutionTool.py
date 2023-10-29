from decimal import Decimal
from math import sqrt


def zero_solution_tool():
	print("\n\n\nZero Solution Tool")
	print('(Only numeric input is supported, otherwise the program will exit automatically.)')
	print("\nPlease enter the coefficient (eg. ax^2 + bx + c = 0).")
	a = Decimal(input("a ="))
	b = Decimal(input("b ="))
	c = Decimal(input("c ="))
	h = Decimal(b * b - 4 * a * c)

	if h < 0:
		print("\nThis equation has no solution, please run the program again and enter the correct coefficient!")

	else:
		d = sqrt(h)
		d0 = Decimal(d)

		def f(x):
			x1 = (- b + d0) / 2 * x
			return x1

		def g(x):
			x2 = (-b - d0) / 2 * x
			return x2
		print("\nresult：\nx1=", f(a), "\nx2=", g(a))

	input("\nPlease press 'Enter' to continue.")
