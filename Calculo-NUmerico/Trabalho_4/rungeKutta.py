def RK4(f):
    return lambda t, y, dt: (
            lambda dy1: (
            lambda dy2: (
            lambda dy3: (
            lambda dy4: (
	    dy1 + 2*dy2 + 2*dy3 + dy4)/6)(dt * f(t + dt, y+dy3)))
	    (dt * f(t + dt/2, y + dy2/2)))(dt * f(t + dt/2, y + dy1/2)))(dt * f(t, y))
#EDO
# y' = t+2ty     y(0) = 3

#Solucao Analitica
#y(t) = (7/2e^(-t*2)) - 0.5

dy = RK4(lambda t, y: t+2*t*y)

t = 0
y = 3

dt = .1

while t <= 10:
    if abs(round(t) - t) < 1e-5:
	print("y(%2.1f)\t= %4.6f" % (t, y))
    t, y = t + dt, y + dy(t, y, dt)
