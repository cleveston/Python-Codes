#Spline Cúbica

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
x = np.linspace(-5, 5, 100)
y = (1/(1 + 25*x**2))
f = interp1d(x, y)

f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(-5, 5, 100)
import matplotlib.pyplot as plt
plt.plot( xnew, f2(xnew),'-')
plt.legend(['cubica'], loc='best')

plt.plot([-10,10],[0,0],color='black')  # Eixo x
plt.plot([0,0],[-10,10],color='black') # Eixo y

plt.ylim(-1,2)  # Limite da janela em y
plt.xlim(-5,5)  # Limite da janela em X.

plt.show()