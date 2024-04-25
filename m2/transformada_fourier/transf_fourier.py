from numpy import where, linspace,  e, fft, pi, array
from plot import add_subplot, imprimir_grafico
import matplotlib.pyplot as plt

x_inicio = -3
x_fim = 3
x_num = 100

t = linspace(x_inicio, x_fim, x_num)

sinal = where(t >= 0, 2*e**(-5*t), 0)

fou_transf = fft.fft(sinal) * (t[1] - t[0])

f = fft.fftfreq(x_num, t[1] - t[0])

module = abs(fou_transf)
if __name__ == "__main__":
    #add_subplot(t, sinal, "sinal em função do tempo", 1)
    #add_subplot(f, module, "sinal no dominio da frequencia", 2)
    #imprimir_grafico()
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(f, module)
    plt.title("sinal no dominio da frequencia")
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.subplot(2, 1, 2)
    plt.plot(t, sinal)
    plt.title("sinal no dominio do tempo")
    plt.xlabel('Tempo (t)')
    plt.ylabel('f(t)')
    plt.grid(True)
    plt.show()