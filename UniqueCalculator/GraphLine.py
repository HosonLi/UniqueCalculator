import numpy as np
import matplotlib.pyplot as plt


def main():
    y = []
    x = []

    xy = []
    x2 = []

    print("\n\nGraph Line")
    print('(Only numeric input is supported, otherwise the program will exit automatically.)')
    print("\nPlease input right number:")
    n = input("n = ")
    for i in range(1, int(n) + 1):
        xn = input("x%d = " %i)
        x.append(float(xn))
    for i in range(1, int(n) + 1):
        yn = input("y%d = " %i)
        y.append(float(yn))

    print("\nResult:")

    ya = np.array(y)
    xa = np.array(x)

    x_mean = np.mean(x)
    print("x-mean =", x_mean)
    y_mean = np.mean(y)
    print("y-mean =", y_mean)

    for i in range(0, int(n)):
        xy.append(x[i] * y[i])
    xy_mean = np.mean(xy)
    print("xy-mean =", xy_mean)

    for i in range(0, int(n)):
        x2.append(x[i] ** 2)
    x2_mean = np.mean(x2)
    print("x2-mean =", x2_mean)

    # print((xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2))

    # Calculate regression coefficient
    slope, intercept = np.polyfit(xa, ya, 1)
    print("k =", slope)
    print("b =", intercept)

    # Draw fitting curve
    plt.scatter(xa, ya)
    plt.plot(xa, slope * xa + intercept, color='red')

    plt.show()

    input("\nPlease press 'Enter' to continue.")
    x.clear()
    y.clear()
    xy.clear()
    x2.clear()
