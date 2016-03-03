import numpy as np

print("------------VERIFICA ORTOGONALIDADE------------")

dim = eval(input("Digite a dimensão da matriz quadrada: "))

ar = []

try:

	for i in range(0, dim):
		t = eval(input("Digite os valores da linha " + str(i+1) + " (separados por vírgula): "))
		ar.append(t)

	ar = np.array(ar)

	print("-------------------------------------------")

	determinante = np.linalg.det(ar)

	if determinante == 1 or determinante == -1:
		print("A matriz é ORTOGONAL")
	else:
		print("A matriz NÃO é ORTOGONAL")

	print("-------------------------------------------")

except:
	print("Erro na matriz.")