# _____________________________________________________________________________
# *****************************************************************************
# Autor: José Antonio Quiñonero gris
# Fecha de creación: 12 de abril de 2022
# *****************************************************************************
# -----------------------------------------------------------------------------

# descripcion del programa

# Librerias
import numpy as np
import matplotlib.pyplot as plt

from config import *

plt.style.use(STYLE_FILE)

# *****************************************************************************
# INICIO
# *****************************************************************************



x, V = np.loadtxt(data("out-potencial_cm-1.dat"), unpack=True, skiprows=2)
n, E, Nconver = np.loadtxt(data("out-conver_energias_cm-1.dat"), unpack=True, skiprows=1)

# print(V)



def Vcalc(x):
    res = (VB/XE**4)*x**4 - (2*VB/XE**2)*x**2 + VB
    return res

def x1(n):
    res = np.sqrt(np.sqrt(E[n]*VB)/VB+1)*XE
    return res
def x2(n):
    res = np.sqrt(1-np.sqrt(E[n]*VB)/VB)*XE
    return res

# GRAFICA
nombre_grafica = 'potencial_doble_pozo_NH3.pdf'

xmax = 1
xmin = -xmax
ymin = 0
ymax = 3000

width  = 6.3
height = width/1.6

fig, ax = plt.subplots(figsize=(width, height))

# Niveles de energia
for i in np.arange(0,len(E)):
    if E[i]<=VB:
        ax.hlines(y = E[i], xmin=-x1(i), xmax=-x2(i), color='black', lw=1.0)
        ax.hlines(y = E[i], xmin=x2(i), xmax=x1(i), color='black', lw=1.0)
    else:
        ax.hlines(y = E[i], xmin=-x1(i), xmax=x1(i), color='black', lw=1.0)

ax.plot(x, V, label=r'$V\,(x)$', color='grey')
# ax.plot(x, Vcalc(x), label=r'$V\,(x)$', color='k')

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)

ax.set(xlabel=r'$x\ (\AA)$', ylabel=r'$E\ (\mathrm{cm^{-1}})$')

# handles, labels = ax.get_legend_handles_labels()
# axs[1].legend(handles[::-1], labels[::-1], loc=(1.01,0.4))
ax.legend(loc='upper right')

plt.savefig(nombre_grafica, transparent='True', bbox_inches='tight')
# plt.show()
