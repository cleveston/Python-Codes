# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:46:36 2014

@author: iury
"""

import matplotlib.pyplot as plt
import numpy as np

campoH = np.array([
3.2,
2.75,
2.29,
1.82,
1.38,
1.03,
0.72,
0.48,
0.31,
0.21,
0.17,
0.13,
0.11,
0.09,
0.07,
0.06,
0.0643,
0.0555,
0.0488,
0.0412,
0.0339,
0.0234,
0.0013
])

campoH = campoH*700

#print(campoH)

campoB = np.array([
220,
210,
200,
190,
180,
170,
160,
150,
140,
130,
120,
110,
100,
90,
80,
70,
60,
50,
40,
30,
20,
10,
0
])

campoB = campoB/(4.44*60*700*3.1415*(10**-7))

#print(campoB)

plt.plot(campoH, campoB, 'ro')
plt.ylabel('Campo B')
plt.xlabel('Campo H')
plt.show()