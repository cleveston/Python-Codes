import matplotlib.pyplot as plt
import numpy as np
from numpy import matrix
from numpy import linalg

print(" matriz: [a  b  c]")
print("         [d  e  f]")
print("         [g  h  i]")
print()

a = eval(input("Insira a: "))
b = eval(input("Insira b: "))
c = eval(input("Insira c: "))
d = eval(input("Insira d: "))
e = eval(input("Insira e: "))
f = eval(input("Insira f: "))
g = eval(input("Insira g: "))
h = eval(input("Insira h: "))
i = eval(input("Insira i: "))

A = matrix([[a,b,c],[d,e,f],[g,h,i]])

print("---------- MATRIZ INSERIDA ----------")
print(A)
print()
print("--------- MATRIZ TRANSPOSTA ---------")
print(A.T)                                  
print()

if(b == d) and (c == g) and (f == h):
    print("Essa matriz é simetrica.")
else:
    print("Matriz assimetrica.")
print()

print("---------- MATRIZ INVERSA -----------")
print(A.I)
print()
