#INSERE A EQUAÇÃO DESEJADA E INFORMA A CÔNICA CORRESPONDENTE - 2D:

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("(----------------CÔNICAS NO PLANO-----------------)")
print()
print("(------- Ax² + Bxy + Cy² + Dx + Ey + F = 0 -------)")
print()

A = eval(input("Insira A: "))
B = eval(input("Insira B: "))
C = eval(input("Insira C: "))
D = eval(input("Insira D: "))
E = eval(input("Insira E: "))
F = eval(input("Insira F: "))

print()
print("(-------------------RESULTADO--------------------)")
print()

if(A == B == C == 0) or (B != 0):
        print("Cônica não encontrada.")

else:
        if(B == D == E == 0) and (F < 0):
                if(A == C) and (A > 0):
                        print("É uma circunferência.")

                elif(A != C) and (A > 0) and (C > 0):
                        print("É uma elipse.")

                elif (A < 0) or (C < 0):
                        print("É uma hipérbole.")
                

        if((A == B == E == F == 0) and (C != 0) and (D != 0)) or ((B == C == D == F == 0) and (A != 0) and (E != 0)):
                print("É uma parábola.")

               
        if(B == D == E == F == 0):
                if(A > 0) and (C > 0):
                        print("É um ponto (elipse degenerada).")

                elif(A < 0) or (C < 0):
                        print("São um par de retas concorrentes (hipérbole degenerada).")


        if((B == C == D == E == 0) and (A > 0) and (F < 0)) or ((A == B == D == E == 0) and (C > 0) and (F < 0)):
                print("São um par de retas paralelas (parábola degenerada).")
        

        if((B == C == D == E == F == 0) and (A != 0)) or ((A == B == D == E == F == 0) and (C != 0)):
                print("É uma reta (parábola degenerada).")



        
        



