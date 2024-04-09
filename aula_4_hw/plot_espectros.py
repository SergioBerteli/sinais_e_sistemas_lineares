from setting import coeficientes_cn, theta
import matplotlib.pyplot as plt

def imprime_espectro_fase():
    x_axis = list(range(len(coeficientes_cn)))
    plt.plot(x_axis, theta, 'ro')
    plt.xlabel("n")
    plt.ylabel("Theta_n")
    plt.title("Espectro de fase")
    plt.grid(True)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.show()

def imprime_espectro_magnitude():
    x_axis = list(range(len(coeficientes_cn)))
    plt.plot(x_axis, coeficientes_cn, 'ro')
    plt.xlabel("n")
    plt.ylabel("C_n")
    plt.title("Espectro de magnitude")
    plt.grid(True)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.show()


if __name__ == "__main__":
    imprime_espectro_magnitude()
    imprime_espectro_fase()
