import matplotlib.pyplot as plt

columns = 1
rows = 2

def add_subplot(x, y, title, n):
    plt.subplot(rows, columns, n)
    plt.stem(x, y)
    plt.title(title)
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("x(t)")

def imprimir_grafico():
    plt.tight_layout()
    plt.show()