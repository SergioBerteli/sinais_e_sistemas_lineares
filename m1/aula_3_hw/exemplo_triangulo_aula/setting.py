from math import pi, sin

t_0 = 2
f_0 = 1/t_0
w_0 = 2*pi*f_0

a_0 = 2

def b_n(n):
    return -4/(n*pi)

def termo(t, n):
    return b_n(n)*sin(n*w_0*t)
