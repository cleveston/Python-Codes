

n, k = input().split()
n = int (n)
k = int (k)
w = list(map(lambda x: int(x), input().split()))

i = 0
subMax = 0
subMaxi = 0
aux = 0
for i in range(n - k + 1):

    aux += w[i + k - 1]

    if (aux > subMax):
        subMax = aux
        subMaxi = i

    aux -= w[i]

print(w[subMaxi + int((k-1)/2)])
