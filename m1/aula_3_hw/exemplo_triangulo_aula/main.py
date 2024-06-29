from setting import w_0, b_n, termo, a_0
from numpy import linspace
import matplotlib.pyplot as plt

n = 100


def f_t(t):
    y = a_0
    for i in range(1, n+1):
        y += termo(t, i)
    return y

if __name__ == "__main__":
    x = linspace(-10, 10, 1000)
    y = [f_t(i) for i in x]
    plt.plot(x, y)
    plt.xlim(-10, 10)
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.show()
