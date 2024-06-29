
from tabulate import tabulate
prev_ns = 2
n_max = 5

impulso = [1 if i==prev_ns else 0 for i in range(n_max+prev_ns)]

degrau = [1 if i>=prev_ns else 0 for i in range(n_max+prev_ns)]

exp = [(1/2)**(i-prev_ns) if i>=prev_ns else 0 for i in range(n_max+prev_ns)]


def primeira_fn_discreta(y, x, n):
    res = x[n] + 0.4*x[n-1] +x[n-2] - 0.25*y[n-1] - 0.1*y[n-2]
    y.append(res)

y = [0 for i in range(prev_ns)]

x = exp

for i in range(n_max):
    primeira_fn_discreta(y, x, i+prev_ns)

headers = ["n", "y(n)", "x(n)"]

table = zip([i for i in range(-prev_ns, n_max)], y, x)

print(tabulate(table, headers))

print(exp)