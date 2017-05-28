#Plotar um vetor em 3D

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

print("")
print("-----------------VETORES----------------")
q = int(input("Quantos Vetores você quer plotar: "))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(q):
	print("--------------------VETOR "+ str(i+1) +"-------------")
	p1 = eval(input("Coordenada do ponto 1 (x,y,z): "))
	p2 = eval(input("Coordenada do ponto 2 (x,y,z): "))
	print("-----------------------------------------------------")
	x1 = np.linspace(p1[0], p2[0], 100)
	y1 = np.linspace(p1[1], p2[1], 100)
	z1 = np.linspace(p1[2], p2[2], 100)
	ax.plot3D(x1,y1,z1, lw=2, label="Vetor "+ str(i+1))
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
