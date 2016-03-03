#Processo de ortogonalização de Gram-Schmidt

import matplotlib.pyplot as plt
import numpy as np


v1= raw_input("Coordenadas  da primeira linha da matriz: (x y z) ")
v2= raw_input("Coordenadas  da segunda linha da matriz: (x y z) ")
v3= raw_input("Coordenadas  da terceira linha da matriz: (x y z) ")


print "Vetor 1: (", v1[0],", ", v2[0],", ", v3[0],")"
print "Vetor 2: (", v1[1],", ", v2[1],", ", v3[1],")"
print "Vetor 3: (", v1[2],", ", v2[2],", ", v3[2],")"

vm1 = [v1[0],v2[0],v3[0]]
vm2 = [v1[1],v2[1],v3[1]]
vm3 = [v1[2],v2[2],v3[2]]


#vetor 1' é igual ao próprio vetor v1
vl1 = vm1
print "Vetor 1': (", vl1[0],",", vl1[1] ,",", vl1[2],")"

#Cálculo do vetor 2' dividido em três partes.

#Primeira parte calcula o produto da linha de cima da fórmula.
vlt = (float(vm2[0])*float(vl1[0])) + (float(vm2[1])*float(vl1[1])) + (float(vm2[2])*float(vl1[2]))

#Depois é dividido pelo linha de baixo da fórmula, resultando assim uma constante.
vltp = (float(vlt))/((float(vl1[0])*float(vl1[0]))+(float(vl1[1])*float(vl1[1]))+(float(vl1[2])*float(vl1[2])))

#A constante multiplica cada uma das coordenadas do vetor v1'.
vl2 = [(float(vm2[0])-(float(vltp)*float(vl1[0]))),(float(vm2[1])-(float(vltp)*float(vl1[1]))),(float(vm2[2])-(float(vltp)*float(vl1[2])))]
print "Vetor 2': (", vl2[0],",", vl2[1] ,",", vl2[2],")"


#Cálculo do vetor 3' dividido em sete partes.

#Primeira parte calcula o produto da linha de cima da fórmula.

vlt1 = ((float(vm3[0])*float(vl1[0]))+(float(vm3[1])*float(vl1[1]))+(float(vm3[2])*float(vl1[2])))
#Depois é dividido pelo linha de baixo da fórmula, resultando assim uma constante.
vlt1p = (float(vlt1))/((float(vl1[0])*float(vl1[0]))+(float(vl1[1])*float(vl1[1]))+(float(vl1[2])*float(vl1[2])))
#A constante multiplica cada uma das coordenadas do vetor v1'.
vl1v = [(float(vlt1p)*float(vl1[0])),(float(vlt1p)*float(vl1[1])),(float(vlt1p)*float(vl1[2]))]

#Primeira parte calcula o produto da linha de cima da fórmula.
vlt2 = ((float(vm3[0])*float(vl2[0]))+(float(vm3[1])*float(vl2[1]))+(float(vm3[2])*float(vl2[2])))
#Depois é dividido pelo linha de baixo da fórmula, resultando assim uma constante.
vlt2p = (float(vlt2))/((float(vl2[0])*float(vl2[0]))+(float(vl2[1])*float(vl2[1]))+(float(vl2[2])*float(vl2[2])))
#A constante multiplica cada uma das coordenadas do vetor v2'.
vl2v = [(float(vlt2p)*float(vl2[0])),(float(vlt2p)*float(vl2[1])),(float(vlt2p)*float(vl2[2]))]

#E por último é diminuído o valor de v3 coordenada a coordenada com os outros dos vetores encontrados anteriormente.
vl3 = [(float(vm3[0])- float(vl2v[0])- float(vl1v[0])),(float(vm3[1])- float(vl2v[1])- float(vl1v[1])),(float(vm3[2])- float(vl2v[2])- float(vl1v[2]))]
print "Vetor 3': (", vl3[0],",", vl3[1] ,",", vl3[2],")"

