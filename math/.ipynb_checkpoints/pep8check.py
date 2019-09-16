% matplotlib
inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


# y = x2 – 1
# exp(x) + x∙(1 – y) = 1 => y = 1 - (1 - exp(x))/x


def drawequations():
    x = np.linspace(-3, 5, 202)
    y1 = np.power(x, 2) - 1
    y2 = 1 - np.divide(1 - np.exp(x), x)
    plt.plot(x, y1, label='Парабола')
    plt.plot(x, y2, label='Экпонента')
    plt.legend()
    plt.grid(True)


def equations(z):
    x, y = z
    return (np.power(x, 2) - 1 - y, np.exp(x) + np.multiply(x, 1 - y) - 1)


x1, y1 = fsolve(equations, (-2, -2))
x2, y2 = fsolve(equations, (2.5, 2.5))
x3, y3 = fsolve(equations, (4, 4))

drawequations()
plt.plot(x1, y1, 'Dm')
plt.plot(x2, y2, 'Dm')
plt.plot(x3, y3, 'Dm')

print(x1, y1)
print(x2, y2)
print(x3, y3)

print(f'Найдено три решения системы уравнений: ({x1}, {y1}), '
      f'({x2}, {y2}), ({x3}, {y3})')