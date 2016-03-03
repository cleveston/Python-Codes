from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("-----------------RETA----------------")
PontoReta = eval(input("Coordenadas do Ponto que pertence a Reta (x, y, z): "))
DiretorReta = eval(input("Coordenadas do Vetor Diretor (x, y, z): "))

x = [PontoReta[0] - DiretorReta[0], PontoReta[0] + DiretorReta[0]]
y = [PontoReta[1] - DiretorReta[1], PontoReta[1] + DiretorReta[1]]
z = [PontoReta[2] - DiretorReta[2], PontoReta[2] + DiretorReta[2]]

reflexar = input("Digite o eixo que você deseja reflexar(x|y|z): ")

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, 'r', lw=1, label="Reta")

if reflexar == 'x':
	reflexao = np.array(x)*-1
	ax.plot(reflexao, y , z, 'b', lw=1, label="Reflexão no Eixo X")
elif reflexar == 'y':
	reflexao = np.array(y)*-1
	ax.plot(x, reflexao , z, 'b', lw=1, label="Reflexão no Eixo Y")
elif reflexar == 'z':
	reflexao = np.array(z)*-1
	ax.plot(x, y , reflexao, 'b', lw=1, label="Reflexão no Eixo Z")

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()