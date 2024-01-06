#=============================================
#  Curvas Z-splines en n dimensiones 
#=============================================
# Julián Sagredo ESFM IPN 2023
#==============================
import numpy as np 
from Curva import Curva,zspline
import matplotlib.pylot as plt
import math

#=====================
# Conjunto de puntos
#=====================
# Número de puntos
nump:np.int32 = 5 
#Dimensión 
dim:np.int32 = 2
# Memoria para puntos
puntos = np.zeros(dim*nump,dtype=np.float64)
# Parametrización
X = np.linspace(0.0,2*np.pi,nump+1)
# Coordenada x 
puntos[0:nump] = np.cos(X[0:nump])  + 0.0*np.sin(2*X[0:nump])
# Coordenada y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#=================================================================
# Curva Z-spline de n puntos zspline(p,d,n,m)
# p: puntos, d: dimensión, n: segmentos de curva, m: continuidad
#=================================================================
n:np.int32 = 1000
x1,y1 = zspline(puntos,dim,n,2)
x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(puntos,dim,n,0)
plt.plot(x3,y3,lw=3,colors="orange")
plt.plot(x2,y2,lw=3,colors="red")
plt.plot(x1,y1,lw=3,colors="blue")
plt.scatter(puntos[0:nump],puntos[nump:2*nump],marker='0',color'black')
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.title("Curva cerrada Z-spline en 2D")
plt.show()