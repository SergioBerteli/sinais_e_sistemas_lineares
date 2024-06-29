from numpy import where, linspace, logical_and, convolve
import matplotlib.pyplot as plt

columns = 1
rows = 3

x_inicio = -3
x_fim = 3
x_num = 10_000

def add_subplot(x, y, title, n):
    plt.subplot(rows, columns, n)
    plt.stem(x, y)
    plt.title(title)
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("x(t)")

t = linspace(x_inicio, x_fim, x_num)
T = t[1] - t[0]

x1 = where(logical_and(t >= 0, t <= 1), 1, 0)

x2 = where(logical_and(t >= -1, t <= 1), 1, 0)

y = convolve(x1, x2, mode="full") * T
ty = linspace(x_inicio*2, x_fim*2, x_num*2-1)

plt.figure(figsize=(10, 6))

add_subplot(t, x1, "Primeiro Gráfico", 1)

add_subplot(t, x2, "Segundo Gráfico", 2)

add_subplot(ty, y, "Resultado da convolução", 3)

plt.tight_layout()
plt.show()
