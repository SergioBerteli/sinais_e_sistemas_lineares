import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode


num = [2500] # numerador da funcao de transferencia
den = [1, 20, 2500] # denominador da funcao de transferencia

ft = TransferFunction(num, den) # cria fn de transferencai

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

plt.show()
