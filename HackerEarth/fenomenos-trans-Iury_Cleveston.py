 
import matplotlib.pyplot as pPlot
import numpy as np
 
pPlot.title('Pressão x Altura')
pPlot.xlabel('Altura(m)')
pPlot.ylabel('Pressão(kPa)')

ro_1 = float(input("Informe a densidade do Fluido 1(Kg/m³): "))
ro_2 = float(input("Informe a densidade do Fluido 1(Kg/m³): "))

gravidade  =  9.8
 
line = np.arange(0,20,0.01)
fluido_1 = line*ro_1*gravidade*10**(-3)
fluido_2 = line*ro_2*gravidade*10**(-3)
 
pPlot.plot(line, fluido_1 , label="Fluido 1")
pPlot.plot(line, fluido_2, label="Fluido 2")
pPlot.show()