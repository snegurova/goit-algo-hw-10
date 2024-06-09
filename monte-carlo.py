"""Module providing a function implementing monte-carlo method."""
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integral(f, a, b, num_samples=10000):
    """Function implementing monte-carlo method"""
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    integral_value = (b - a) * np.mean(y_random)
    return integral_value

# Обчислення інтеграла методом Монте-Карло
mc_result = monte_carlo_integral(f, a, b)
print("Інтеграл методом Монте-Карло:", mc_result)

# Аналітичне обчислення інтеграла
analytical_result, error = spi.quad(f, a, b)
print("Аналітичний інтеграл:", analytical_result)
print("Абсолютна помилка:", abs(mc_result - analytical_result))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
