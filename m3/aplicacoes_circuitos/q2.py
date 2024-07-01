from numpy import real, imag, e, linspace, roots
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

def resp_tempo(t, r, c):
    if (t > 0):
        return (e**(-t/(r*c)))
    return 0

res = float(input("Insira o valor da resistência: "))
cap = float(input("Insira o valor da capacitancia (em micro): "))
cap = cap * 10**-6
numerador = [1, 0 ] # 1s

denominador = [1, 1/(res*cap)] # s + 1/(rc)


zeros = roots(numerador)
polos = roots(denominador)

print(zeros, polos)

# plot da função de transferência

a = r'H(S) = \frac{s}{s + '+str(denominador[1])+r'}'
ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
plt.text(0.4,0.4,'$%s$' %a,size=50,color="green")
plt.title("Função de transferencia")

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
w = linspace(10**-1, 10**3, 10**4)
w, A, fase = bode(ft, w=w)

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


t = linspace(-5, 5, 100000)
degrau = [1 if i>=0 else 0 for i in t]
y = [resp_tempo(i, res, cap) for i in t]


plt.figure()
plt.plot(t, y, label="Tensão de saída", color="green", linewidth=4)
plt.plot(t, degrau, color="red",  label="Tensão de entrada (degrau)")
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.xlabel('Tempo')
plt.ylabel('Tensão de saída')
plt.title('Resposta do circuito ao degrau')
plt.legend()
plt.show()