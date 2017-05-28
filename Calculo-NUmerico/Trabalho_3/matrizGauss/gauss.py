# -*- coding: latin1 -*-

import numpy
from fractions import Fraction as f

def lerMatrix(m):
    file_obj = open("matrix" + m +  ".txt") 
    matrix = [] 
    ordem = 0
    matrix_append = matrix.append 
    for line in file_obj:
      ordem = ordem + 1
      matrix_append([f(x) for x in line.split() if x]) 
   
    file_obj = open("matrixIndependente" + m + ".txt") 
    data = [] 
    data_append = data.append 
    for line in file_obj:
      data_append([f(x) for x in line.split() if x]) 
      
    return [matrix, data, ordem]

def calculaX(mA,x,j,k):
    if (j == k):
        k -= 1
    if (k < 0):
        return 0
    return f(mA[j][k])*f(x[k]) + calculaX(mA,x,j,k-1)

def defineMatriz():
    m = str(input("Escolha a matrix(1, 2): "))
    if m > '2' or m < '1':
      print("Opcao invalida.")
      exit(1)
    dados = lerMatrix(m)
    matriz = dados[0]
    independentes = dados[1]
    ordem = int(dados[2])
    x = []
    
    for i in range(ordem):
        x.append('1')
    
    k = ordem
    lista = []
    nI = 0
    passo = 1
    while k > 0:
        i = ordem - k
        den = matriz[ordem-k][ordem-k]

        if (den == 0):
            if (i == 0):
                print ('Resultado Impossivel')
                break
            lista = matriz[i+1]
            matriz[i+1] = matriz[i]
            matriz[i] = lista
            nI = independentes[i+1]
            independentes[i+1] = independentes[i]
            independentes[i] = nI
            if (den == 0):
                print ('Resultado Impossivel')
                break
        while i+1 < ordem:
            contador = 0
            j = ordem - k + 1
            num = matriz[i+1][ordem-k]
            divisor = num/den
            while contador < ordem:
                if (j > ordem):
                    break
                matriz[i+1][j-1] = matriz[i+1][j-1] - matriz[ordem-k][j-1] * divisor
                j += 1
                contador += 1
            independentes[i+1][0] = independentes[i+1][0] - independentes[ordem-k][0] * divisor
            i += 1
            passo += 1
        k = k - 1
    else:
        c = 0
        k = ordem-1
        while c < ordem:
            termo = calculaX(matriz,x,k-c,k)
            if (matriz[k-c][k-c] == 0):
                print ('Resultado Impossivel')
                break
            else:
                x[k-c] = (independentes[k-c][0] - termo)/matriz[k-c][k-c]
                c += 1
        else:
            print ('\nResultado para X: ')
           
            for s in x:
                print(float(round(s, 6)))
                
            print ('\nMatrix Inversa para X: ')
            inv = numpy.linalg.inv(matriz)
            for s in inv:
              for j in s:
                print(round(j , 3) , end='  ')
              print("\n")
                           
if __name__ == '__main__':
	defineMatriz()
