import numpy
import math

def main():
    x = []
    dx2 = []

    print('\n\nData Processing')
    print('(Only numeric input is supported, otherwise the program will exit automatically.)')
    print("\nPlease input right number:")
    n = input("n = ")
    for i in range(1, int(n) + 1):
        xn = input("x%d = " % i)
        x.append(float(xn))
    print("\n---------------------")
    print("1. Instrumental Error")
    print("2. Minimum Graduation Value")
    choose_ub = input("Choose the B-type uncertainty calculation method：")
    if choose_ub == '1':
        instrumental_error = input("\ninstrumental error = ")
        ub = float(instrumental_error) / math.sqrt(3)
    elif choose_ub == '2':
        minimum_graduation_value = input("\nminimum graduation value = ")
        ub = float(minimum_graduation_value) / math.sqrt(12)
    else:
        print("\nPlease restart this!")
        return
    print("\nResult:")
    x_mean = numpy.mean(x)
    print("mean =", x_mean)
    for i in range(0, int(n)):
        dx2n = (x[i] - x_mean) ** 2
        print("dx2%d =" % (i + 1), dx2n)
        dx2.append(dx2n)
    s = math.sqrt(numpy.sum(dx2) / (int(n) - 1))
    print("S =", s)
    ua = s / math.sqrt(int(n))
    print("ua =", ua)
    print("ub =", ub)
    u = math.sqrt(ua ** 2 + ub ** 2)
    print("u =", u)
    print("x =", x_mean, "+-", u)

    input("\nPlease press 'Enter' to continue.")
    x.clear()
    dx2.clear()
