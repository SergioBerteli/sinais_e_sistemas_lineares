from numpy import real, imag, e, linspace, roots, cos
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

numerador = [2500] # 2500
denominador = [1, 20, 2500] # s^2 + 20 * s+ 2500

zeros = roots(numerador)
polos = roots(denominador)

print(zeros, polos)

# plot da função de transferência

a = r'H(S) = \frac{'+str(numerador[0])+r'}{s^2 + s * '+str(denominador[1])+r' + '+str(denominador[2])+r'}'
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

plt.show()