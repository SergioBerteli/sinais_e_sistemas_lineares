
from numpy import real, imag, e, linspace, roots
import matplotlib.pyplot as plt

numerador = [0.2, 0.1] # 1(rc)

denominador = [1, 0.7, -0.5] # s + 1/(rc)


zeros = roots(numerador)
polos = roots(denominador)

print(zeros, polos)

# plot do gráfico

plt.figure()
plt.scatter(real(zeros), imag(zeros), marker='o', color='blue', label='Zeros')
plt.scatter(real(polos), imag(polos), marker='x', color='red', label='Polos')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.title('Polos e zeros da função de transferência')
plt.legend()
plt.show()
