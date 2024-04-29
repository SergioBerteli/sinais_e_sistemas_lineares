from numpy import where, linspace,  e, fft, abs as absnp, angle
import matplotlib.pyplot as plt

x_inicio = -3
x_fim = 3
x_num = 100

t = linspace(x_inicio, x_fim, x_num)

sinal = where(t >= 0, 2*e**(-5*t), 0)

fou_transf = fft.fft(sinal) * (t[1] - t[0])

f = fft.fftfreq(x_num, t[1] - t[0])

module = absnp(fou_transf)
phase = angle(fou_transf)

if __name__ == "__main__":
    #add_subplot(t, sinal, "sinal em função do tempo", 1)
    #add_subplot(f, module, "sinal no dominio da frequencia", 2)
    #imprimir_grafico()
    # plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, sinal)
    plt.title("Modulo do sinal no dominio da frequencia")
    plt.xlabel('Tempo (t)')
    plt.ylabel('f(t)')
    plt.grid(True)
    plt.subplot(3, 1, 2)
    plt.plot(f, module)
    plt.title("Sinal no dominio da frequencia")
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.subplot(3, 1, 3)
    plt.plot(f, phase)
    plt.title("Fase do sinal no dominio da frequencia")
    plt.xlabel('Frequencia (Hz)')
    plt.ylabel('Fase')
    plt.grid(True)
    
    plt.subplots_adjust(hspace=0.5)

    plt.show()