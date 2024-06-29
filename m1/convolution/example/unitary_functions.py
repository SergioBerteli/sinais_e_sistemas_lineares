from numpy import linspace, where, logical_and
import matplotlib.pyplot as plt

n = 10_000
tf = 6

t = linspace(0, tf, n)

x1 = where(logical_and(t>=0 , t<=2), 3*t, 0)

x2 = where(logical_and(2*t>=0, 2*t<=2), 3*(2*t), 0)

plt.figure(figsize=(10,6))

plt.subplot(3, 1, 1)
plt.stem(t, x1)
plt.grid(True)
plt.ylabel("x(t)")
plt.xlabel("t")
plt.title("Primeiro gráfico")


plt.subplot(3, 1, 2)
plt.stem(t, x2)
plt.grid(True)
plt.ylabel("x(t)")
plt.xlabel("t")
plt.title("Segundo gráfico")

plt.tight_layout()
plt.show()
