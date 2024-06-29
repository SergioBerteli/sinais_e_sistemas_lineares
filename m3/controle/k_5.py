import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode, tf2zpk, step
from numpy import linspace, cos, e

k = 5

num = [k, 2*k] # numerador da funcao de transferencia
den = [1, 2+k, 2*k + 3] # denominador da funcao de transferencia

zeros, polos, _ = tf2zpk(num, den)
print(f"zeros: {zeros}")
print(f"polos: {polos}")

ft = TransferFunction(num, den) # cria fn de transferencai

t, y = step(ft)

plt.figure()
plt.plot(t, y)
plt.xlabel('S')
plt.ylabel('Amplitude')
plt.title('Resposta ao degrau no dominio de Laplace')
plt.grid()

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


t = linspace(0, 100, 10000)

y = 10/13+2.78*e**(-3.5*t)*cos(3**0.5/2*t+253.9)

plt.figure()
plt.plot(t, y)
plt.xlabel("tempo (s)")
plt.ylabel("Y")
plt.title("Resposta do sistema para o degrau no tempo")
plt.grid(which='both', axis='both')

plt.show()
