from numpy import real, imag, e, linspace, roots
import matplotlib.pyplot as plt

def resp_tempo(t, r, c):
    if (t > 0):
        return (1- e**(-t/(r*c)))
    return 0

res = float(input("Insira o valor da resistência: "))
cap = float(input("Insira o valor da capacitancia: "))

numerador = [1/(res*cap)] # 1(rc)

denominador = [1, 1/(res*cap)] # s + 1/(rc)


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

t = linspace(-5, 5, 400)
y = [resp_tempo(i, res, cap) for i in t]

plt.figure()
plt.plot(t, y)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid(True, which='both', linestyle='--', lw=0.5)
plt.xlabel('Tempo')
plt.ylabel('Tensão de saída')
plt.title('Resposta do circuito ao degrau')
plt.show()