from numpy import real, imag, e, linspace, roots
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

def resp_tempo(t, r, l):
    if (t > 0):
        return (e**(-t*r/(l)))
    return 0

res = float(input("Insira o valor da resistência: "))
ind = float(input("Insira o valor da indutância: "))

numerador = [1*ind*res, 0 ] # 1s*l*r

denominador = [1*ind, res] # s*l + r


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


t = linspace(-5, 5, 400)
y = [resp_tempo(i, res, ind) for i in t]

plt.figure()
plt.plot(t, y)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.xlabel('Tempo')
plt.ylabel('Tensão de saída')
plt.title('Resposta do circuito ao degrau')
plt.show()