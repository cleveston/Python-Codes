import string
x = input("Digite o número em Ponto Flutuante: ")

c = x.split('.');

binG = str(bin(int(c[0])))

binP = str(bin(int(c[1])))

print("Número em Binário: " + binG[2:] + "." + binP[2:])
