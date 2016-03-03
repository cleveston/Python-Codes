 
# -*- coding: iso-8859-1 -*-
"""
Created on Sat May 24 17:13:35 2014

@author: iury
"""

import numpy as np

eo = 8.854e-12
muo = np.pi*4*e-7

print("\n")
print("------------CABO COAXIAL-------------")

raioI = float(input("Digite o raio interno (mm): "))
raioE = float(input("Digite o raio externo (mm): "))
permissividadeR = float(input("Digite a permissividade relativa: "))
condutividadeD = float(input("Digite a conditividade do dieletrico (S/m): "))
condutividadeC = float(input("Digite a conditividade do condutor (S/m): "))
frequencia = float(input("Digite a frequencia (Hz): "))

omega = 2*np.pi*frequencia

G = (2*np.pi*condutividadeD)/(np.log(raioE/raioI))
C = (2*np.pi*permissividadeR*eo)/(np.log(raioE/raioI))
L = muo*np.log(raioE/raioI)/(2*np.pi)
Rs = np.sqrt(np.pi*frequencia*muo/condutividadeC)
R = (1000*((1/raioI) + (1/raioE))*Rs)/(2*np.pi)
gamma = np.sqrt((R + 1j*omega*L)*(G + 1j*omega*C))

print("\n")
print("-------------RESULTADOS-------------")
print("G = " + str(G) + " S/m")
print("C = " + str(C) + " F/m")
print("L = " + str(L) +  " H/m")
print("R = " + str(R) + " ohm/m")
print("Constante de Propagacao (Gamma) = " + str(gamma))