

h1, t1 = input().split()
h2, t2 = input().split()
h3, t3 = input().split()
h4, t4 = input().split()

times = {
    1: (int(h1), int(t1), int(h1) + int(t1)),
    2: (int(h2), int(t2), int(h2) + int(t2)),
    3: (int(h3), int(t3), int(h3) + int(t3)),
    4: (int(h4), int(t4), int(h4) + int(t4)),
}

if (times[1][2]) >= (times[2][2]):
    index = 1
    adversario = times[2][1]
else:
    index = 2
    adversario = times[2][1]

a1 = (index, adversario)

if (times[3][2]) >= (times[4][2]):
    index = 3
    adversario = times[4][1]
else:
    index = 4
    adversario = times[3][1]

a2 = (index, adversario)

if (times[a1[0]][2] + a2[1]) >= (times[a2[0]][2] + a1[1]):
    print(a1[0])
else:
    print(a2[0])
