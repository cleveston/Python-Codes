
import math
import numpy as np

def f_of_t(t):
  return t**2


def simpson(f, a, b, n):
    if n & 1:
        print("Numero de repeticoes precisa ser par.")
        return 0.0

    h = (b - a) / n
    integral = 0.0

    x = a
    for i in range(0, n/2):
        integral += f(x) + (2.0 * f(x + h))
        x += 2 * h

    integral = (2.0 * integral) - f(a) + f(b)
    integral = h * integral / 3.0
    return integral

a = input("Limite inferior: ")
b = input("Limite superior: ")
n = input("Numero de repeticoes: ")

print(simpson(f_of_t, float(a), float(b), int(n)))


