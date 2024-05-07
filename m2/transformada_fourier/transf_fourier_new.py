from numpy import where, linspace,  e, fft, abs as absnp, angle, arctan
import matplotlib.pyplot as plt


def calcula_modulo(w):
    return 1/((1-w**2)**2+(2*w)**2)**0.5

def calcula_fase(w):
    return -arctan(w*2/(1-w**2))

x_inicio = -3
x_fim = 3
x_num = 100

t = linspace(x_inicio, x_fim, x_num)
dx = t[1] - t[0]

sinal = where(t >= 0, t*e**-t, 0)

module = [calcula_modulo(i) for i in t]
phase = [calcula_fase(i) for i in t]

if __name__ == "__main__":
    plt.subplot(3, 1, 1)
    plt.plot(t, sinal)
    plt.title("Modulo do sinal no dominio do tempo")
    plt.xlabel('Tempo (t)')
    plt.ylabel('f(t)')
    plt.grid(True)
    plt.subplot(3, 1, 2)
    plt.plot(t, module)
    plt.title("Sinal no dominio da frequencia")
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.subplot(3, 1, 3)
    plt.plot(t, phase)
    plt.title("Fase do sinal no dominio da frequencia")
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Fase')
    plt.grid(True)
    
    plt.subplots_adjust(hspace=0.5)

    plt.show()