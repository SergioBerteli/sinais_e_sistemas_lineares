from numpy import real, imag, e, linspace, roots
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode, step

def resp_tempo(t):
    if (t > 0):
        return -0.03*e**(-5.13*t)+1.03*e**(-194.9*t)
    return 0

res = float(input("Insira o valor da resistência: "))
ind = float(input("Insira o valor da indutância: "))
cap = float(input("Insira o valor da capacitancia: "))

numerador = [1, 0, 0 ] # 1s^2

denominador = [1, res/ind, 1/(ind*cap)] # s^2+r*s/l+1/(rl)


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

# Bode


ft = TransferFunction(numerador, denominador) # cria fn de transferencai

w, A, fase = bode(ft)

plt.figure()
plt.semilogx(w, A)  
plt.title('Diagrama de bode - ganho em db')
plt.xlabel('W')
plt.ylabel('Ganho [dB]')
plt.grid(which='both', axis='both')

plt.figure()
plt.semilogx(w, fase)  
plt.title('Diagrama de bode - fase')
plt.xlabel('W')
plt.ylabel('Fase')
plt.grid(which='both', axis='both')

# resposta ao step em laplace

t, y = step(ft)

plt.figure()
plt.plot(t, y)
plt.xlabel('S')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau no dominio de Laplace')
plt.grid()

# resposta ao step com r = 2. c = 0.1, l = 0.01

t = linspace(-5, 5, 400)
y = [resp_tempo(i) for i in t]

plt.figure()
plt.plot(t, y)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.xlabel('Tempo')
plt.ylabel('Tensão de saída')
plt.title('Resposta do circuito ao degrau no tempo com r = 2, c = 0.1, l = 0.01')

plt.show()