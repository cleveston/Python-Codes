
#Verificar se é L.I. ou L.D no R³.

import matplotlib.pyplot as plt
import numpy as np
print("")
print("-------------------LD ou LI------------------")
v1= eval(input("Coordenadas do ponto 1 (x,y,z): "))
v2= eval(input("Coordenadas do ponto 2 (x,y,z): "))
v3= eval(input("Coordenadas do ponto 2 (x,y,z): "))

det = np.linalg.det([v1,v2,v3])

print("---------------------------------------------")

if det == 0.0:
    print("Sistema Linearmente Dependente")
else:
    print("Sistema Linearmente Independente")

print("---------------------------------------------")