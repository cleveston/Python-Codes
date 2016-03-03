#Plotar um vetor em 2D

import matplotlib.pyplot as plt
import numpy as np

print("")
print("-----------------VETORES----------------")
q = int(input("Quantos Vetores você quer plotar: "))

for i in range(q):
	print("--------------------VETOR "+ str(i+1) +"-------------")
	p1 = eval(input("Coordenada do ponto 1 (x,y): "))
	p2 = eval(input("Coordenada do ponto 2 (x,y): "))
	print("-----------------------------------------------------")
	x1 = np.linspace(p1[0], p2[0], 100)
	y1 = np.linspace(p1[1], p2[1], 100)
	plt.plot(x1,y1, lw=2, label="Vetor "+ str(i+1))
plt.legend()
plt.show()