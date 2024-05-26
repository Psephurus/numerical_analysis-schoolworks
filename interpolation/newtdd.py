import numpy as np
import matplotlib.pyplot as plt
from nest import nest

def newtdd(x, y, n):
    v = [[0] * n for _ in range(n)]
    for j in range(n):
        v[j][0] = y[j]
    for i in range(1, n):
        for j in range(n - i):
            v[j][i] = (v[j + 1][i - 1] - v[j][i - 1]) / (x[j + i] - x[j])
    c = [v[0][i] for i in range(n)]
    return c

x0 = np.array([0, 2, 3])
y0 = np.array([1, 2, 4])
c = newtdd(x0, y0, 3)
x = np.linspace(0,4,400)
y = nest(2, c, x, x0)
plt.scatter(x0, y0)
plt.plot(x,y)
plt.show()
