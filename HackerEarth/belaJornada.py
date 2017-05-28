n = int(input())
a = list(map(lambda x: int(x), input().split()))

valor = [0 for x in range(n-1)]

for i in range(n-1):

    s1 = sum(a[i::-1])
    s2 = sum(a[:i:-1])

    valor[i] = s1*s2

print(max(valor))
