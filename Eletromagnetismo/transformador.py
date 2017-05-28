# -*- coding: iso-8859-1 -*-
"""
Created on Sat May 24 17:13:35 2014

@author: iury
"""
import numpy as np

matNucleo = [1, 0.4]

print("\n--------------TRANSFORMADOR----------------")
print("---------------------------------------------")
tensaoIn = int(input("Informe a tensao de entrada(V): "))
tensaoOut = int(input("Informe a tensao de saida(V): "))
potenciaOut = int(input("Informe a potencia de saida(Watts): "))
rendimento = int(input("Informe o rendimento(%): "))
frequencia = int(input("Informe a frequencia(Hz): "))
nucleo = int(input("Escolha o material do nucleo( 1 - Ferrite, 2 - Laminado): "))

potenciaIn = (1+(1-(rendimento/100)))*potenciaOut

secaoNucleo = int(np.ceil(np.sqrt(potenciaIn)))

nPrincipal = int(np.ceil((tensaoIn*10000)/(4.44*matNucleo[nucleo-1]*frequencia*secaoNucleo)))

nSecundario = int(np.ceil(nPrincipal/(tensaoIn/tensaoOut)))

i1 = np.ceil(potenciaIn/tensaoIn)
i2 = np.ceil(potenciaOut/tensaoOut)
condutor1 = np.ceil(i1/3)
condutor2 = np.ceil(i2/3)

print("----------------RESULTADO-------------------")
print("--------------------------------------------")
print("Secao do Nucleo: ", secaoNucleo, " cm2")
print("Bobina principal: ", nPrincipal, " voltas")
print("Bobina Secundaria: ", nSecundario, " voltas")
print("Secao do condutor 1: ", condutor1, " mm2") 
print("Secao do condutor 2: ", condutor2, " mm2") 