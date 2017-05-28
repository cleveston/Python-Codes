# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 11:23:26 2014

@author: iury
"""

import matplotlib.pyplot as pPlot
import numpy as np

def maior(x,y): #Aqui definimos a função MAIOR, essa função é uma função de x e y
  if x>y: # Comparamos x e y, se x é maior retornamos o valor de x
    return x
  else: # caso contrário, retornamos o valor de y
    return y

amplitudeP = float((input("Amplitude em z=0 - Onda Progressiva: ")))
amplitudeR = float(input("Amplitude em z=0 - Onda Regressiva: "))
amortecimento = float(input("Amortecimento (Alfa): "))
cFase = float(input("Constante de Fase (Beta): "))
frequencia = float(input("Frequencia (Hz): "))

omega = 2*np.pi*frequencia

x = linspace(0, 50*np.pi/omega, 101)
x1 = linspace(0, 50*np.pi/omega, 103)
progressiva = amplitudeP*np.e**(-amortecimento*x)*np.cos(omega*x - cFase*x)
regressiva = amplitudeR*e**(amortecimento*x1)*np.cos(omega*x1 + cFase*x1)


title('Ondas')
xlabel('Espaco')
ylabel('Amplitude')
ylim(-maior(amplitudeP, amplitudeR) - (maior(amplitudeP, amplitudeR)/3),
     maior(amplitudeP, amplitudeR) + (maior(amplitudeP, amplitudeR)/3))
xlim(0, 50*np.pi/omega)
grid()

plot(x, progressiva)
plot(x1, regressiva)


