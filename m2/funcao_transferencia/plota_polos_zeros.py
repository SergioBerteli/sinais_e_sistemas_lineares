from numpy import real, imag
from scipy import signal
import matplotlib.pyplot as plt

numerador = [1, 3, 2] # s^2 + 3*s + 2

denominador = [1, 6, 11, 6] # s^3 + 6*s^2 + 11*s + 6

# criando a função de transferencia

fn_transf = signal.TransferFunction(numerador, denominador)

zeros, polos, ganho = signal.tf2zpk(numerador, denominador)

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