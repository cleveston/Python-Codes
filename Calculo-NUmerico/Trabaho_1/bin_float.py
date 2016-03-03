import string
x = input("Digite o número em Binário: ")

c = x.split('.');

binG = str(int(c[0], 2))

binP = str(int(c[1], 2))

print("Número em Decimal: " + binG + "." + binP)
