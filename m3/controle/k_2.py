from numpy import real, imag, e, linspace, roots, cos
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

k = 2

def resp_tempo_1(t):
    if (t > 0):
        return  4/7+0.76*e**(-2*t)*cos(3**0.5*t+139)
    return 0

numerador = [k, 2*k] # numerador da funcao de transferencia
denominador = [1, 2+k, 2*k + 3] # denominador da funcao de transferencia

zeros = roots(numerador)
polos = roots(denominador)

print(zeros, polos)

# plot da função de transferência

a = r'H(S) = \frac{(s + 2) * '+str(k)+r'}{s^2 + s * '+str(denominador[1]) +r' + '+str(denominador[2])+r'}'
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

# Bode


ft = TransferFunction(numerador, denominador) # cria fn de transferencai
w = linspace(10**-2, 10**4, 10**5)
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

# resposta ao degrau

t = linspace(-5, 5, 100000)
degrau = [1 if i>=0 else 0 for i in t]
y = [resp_tempo_1(i) for i in t]

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