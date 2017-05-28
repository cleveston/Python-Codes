from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

def distPontos():
	print("-----------------PONTO A----------------")
	PontoA = eval(input("Digite as coordenadas (x, y, z): "))
	print("")
	print("-----------------PONTO B----------------")
	PontoB = eval(input("Digite as coordenadas(x, y, z): "))
	print("----------------------------------------")
	dist = round(np.linalg.norm(np.array(PontoB)-np.array(PontoA)), 3)
	print("Distância de A a B: ", dist)
	print("----------------------------------------")
	input()
	plotar = input("Deseja Plotar o Gráfico (s/n): ")

	if plotar == 's':
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		ax.plot([PontoA[0]], [PontoA[1]], [PontoA[2]], 'ro', label="Ponto A "+ str(PontoA))
		ax.plot([PontoB[0]], [PontoB[1]], [PontoB[2]], 'bo', label="Ponto B "+ str(PontoB))
		ax.plot([PontoA[0], PontoB[0]], [PontoA[1], PontoB[1]], [PontoA[2], PontoB[2]], 'b', lw=1, label="Distância "+ str(dist))
		ax.legend()
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.show()
	
def distPontoReta():
	print("-----------------PONTO----------------")
	Ponto = eval(input("Coordenadas do Ponto (x, y, z): "))
	print("")
	print("-----------------RETA----------------")
	PontoReta = eval(input("Coordenadas do Ponto que pertence a Reta (x, y, z): "))
	DiretorReta = eval(input("Coordenadas do Vetor Diretor (x, y, z): "))

	PontoAP = np.array(Ponto) - np.array(PontoReta)
	x = -(PontoAP[1]*DiretorReta[2] - DiretorReta[1]* PontoAP[2])
	y = PontoAP[0]*DiretorReta[2] - DiretorReta[0]* PontoAP[2]
	z = -(PontoAP[0]*DiretorReta[1] - DiretorReta[0]* PontoAP[1])
	norma1 = norma(x, y, z)
	norma2 = norma(DiretorReta[0], DiretorReta[1], DiretorReta[2])

	dist = round(norma1/norma2, 3)
	print("Distância do Ponto a Reta: ", dist)
	print("----------------------------------------")
	input()
	plotar = input("Deseja Plotar o Gráfico (s/n): ")

	if plotar == 's':
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		ax.plot([Ponto[0]], [Ponto[1]], [Ponto[2]], 'ro', label="Ponto "+str(Ponto))
		ax.plot([PontoReta[0] - DiretorReta[0], PontoReta[0] + DiretorReta[0]], [PontoReta[1] - DiretorReta[1], PontoReta[1]+ DiretorReta[1]*2],
		 [PontoReta[2] - DiretorReta[2], PontoReta[2]+ DiretorReta[2]], 'b', lw=1, label="Reta")
		ax.legend()
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.show()

def distPontoPlano():
	print("-----------------PONTO----------------")
	Ponto = eval(input("Coordenadas do Ponto (x, y, z): "))
	print("")
	print("-----------------PLANO----------------")
	plano = eval(input("Coordenadas do Plano (a, b, c, d): "))

	norma1 = norma(plano[0]* Ponto[0], plano[1]*Ponto[1], plano[2]*Ponto[2])
	norma2 = norma(plano[0], plano[1], plano[2])

	dist = round(norma1/norma2, 3)
	print("Distância do Ponto ao Plano: ", dist)
	print("----------------------------------------")
	input()
	plotar = input("Deseja Plotar o Gráfico (s/n): ")
	if plotar == 's':
		PlotarPlano(Ponto[0], Ponto[1], Ponto[2], plano[0], plano[1], plano[2], plano[3])

def norma(x,y,z):
	return np.linalg.norm([x,y,z])

def PlotarPlano(x1,y1,z1,x2,y2,z2,d):
	ponto  = np.array([x1,y1,z1])
	normal = np.array([x2,y2,z2])
	x, y = np.meshgrid(range(10), range(10))
	z = (-normal[0]*x - normal[1]*y - d)/normal[2]
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.plot([x1], [y1], [z1], 'ro', label="Ponto")
	ax.plot_surface(x,y,z, label ='Plano')
	ax.legend()
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()

print("----------------------------------------")
print("-----------------OPÇÕES-----------------")
print("1 - Distância entre dois pontos")
print("2 - Distância entre ponto e reta")
print("3 - Distância entre ponto e plano")
print("----------------------------------------")
opcao = int(input("Digite sua opção: "))

if opcao == 1:
	distPontos()
elif opcao == 2:
	distPontoReta()
elif opcao == 3:
	distPontoPlano()
