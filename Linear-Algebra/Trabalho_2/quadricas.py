from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def esfera(meia):
    fig = plt.figure(figsize=plt.figaspect(1)) 
    ax = fig.add_subplot(111, projection='3d')  

    vx= eval(input("Raio da esfera(r): "))
    coefs = (vx, vx, vx)  
    rx, ry, rz = [1/np.sqrt(coef) for coef in coefs]

    if meia == 1:
        u = np.linspace(0,1 * np.pi, 100)
    else:
        u = np.linspace(0,2 * np.pi, 100)
    v = np.linspace(0,  np.pi, 100)

    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))


    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

    max_radius = max(rx, ry, rz)
    for axis in 'xyz':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

    plt.show()

def elipsoide(meia):
    fig = plt.figure(figsize=plt.figaspect(1)) 
    ax = fig.add_subplot(111, projection='3d')

    vx= eval(input("Dimensões da elipsoide(a,b,c): "))

    coefs = (vx[0], vx[1], vx[2])  
    rx, ry, rz = [1/np.sqrt(coef) for coef in coefs]

    if meia == 3:
        u = np.linspace(0,1 * np.pi, 100)
    else:
        u = np.linspace(0,2 * np.pi, 100)
    v = np.linspace(0,  np.pi, 100)

    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

    max_radius = max(rx, ry, rz)
    for axis in 'xyz':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

    plt.show()

def hiperboloide(meia):
    fig = plt.figure(figsize=plt.figaspect(1)) 
    ax = fig.add_subplot(111, projection='3d')
    
    u=np.linspace(-2,2,100)

    if meia==5:
        v=np.linspace(0,1*np.pi,60)
    else:
        v=np.linspace(0,2*np.pi,60)
        
    [u,v]=np.meshgrid(u,v)

    vx= eval(input("Dimensões da elipsoide(a,b,c): "))

    x = vx[0]*np.cosh(u)*np.cos(v)
    y = vx[1]*np.cosh(u)*np.sin(v)
    z = vx[2]*np.sinh(u)

    ax.plot_surface(x, y, z,  rstride=3, cstride=3, color='b')

    plt.show()
    
op = 0
while op != 7:
    print("------------Menu-----------")
    print("1 - Plotar meia esfera")
    print("2 - Plotar uma esfera")
    print("3 - Plotar meia elipsoide")
    print("4 - Plotar uma elipsoide")
    print("5 - Plotar meia hiperboloide")
    print("6 - Plotar uma hiperboloide")
    print("7 - Sair")
    print("---------------------------")
    op = eval(input("Escolha sua opcao: "))

    if op==1 or op==2:
        esfera(op)

    elif op==3 or op==4:
        elipsoide(op)

    elif op==5 or op==6:
        hiperboloide(op)