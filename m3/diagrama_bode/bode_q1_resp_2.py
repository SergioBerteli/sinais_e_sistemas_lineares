import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, arctan2

w = 5 # frequencia em rad/

t = linspace(0, 10, 100)

y = 100*w/(w**2+100**2)**0.5*cos(5000*t+10+90-arctan2(w, 100))

plt.figure()
plt.plot(t, y)
plt.xlabel("tempo (s)")
plt.ylabel("Y")
plt.title("Resposta do sistema para uma entrada x(t) = 100*cos(5000t+10)")
plt.grid(which='both', axis='both')

plt.show()
