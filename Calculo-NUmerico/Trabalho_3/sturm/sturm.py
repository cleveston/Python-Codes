#Sturm para polinômios de 3º grau 

import numpy as np

matriz = []

matriz.append(eval(input("Informe os coeficientes do polinômio: ")))

a = eval(input("Entre com o limite inferior: "))
b = eval(input("Entre com o limite superior: "))

size = len(matriz[0])
ordem = size -2

matriz.append(np.polyder(matriz[0]))

i = 0
while ordem:
  matriz.append(np.polydiv(matriz[i], matriz[i+1])[1]*-1)
  i += 1
  ordem -= 1

i = 0
mul = size - 1

resultadoA = []
resultadoB = []

while size:
  resultadoA.append(np.polyval(matriz[i], a))
  resultadoB.append(np.polyval(matriz[i], b))
  i += 1
  size -= 1

i = 0
sa = 0
sb = 0
while mul:

  if float(resultadoA[i])*float(resultadoA[i + 1]) < 0:
      sa = sa+1
  if float(resultadoB[i])*float(resultadoB[i + 1]) < 0:
      sb = sb+1
  
  i += 1
  mul -= 1
  
dim = abs(sa-sb)

if sa == sb:
  print("Não possui raízes reais no intervalo.")
else:
  print("Possui ",dim, " raízes reais no intervalo")