# _____________________________________________________________________________
# Wavefunctions and potential plot for NH3/ND3 double well
#
# Usage:
#   cd examples/NH3
#   python ../../grafica/funciones_y_potencial.py
#
#   Or specify output directory:
#   python ../../grafica/funciones_y_potencial.py --output ../ND3/output
#
# Generates: funciones_y_potencial.pdf in current directory
# _____________________________________________________________________________
# Autor: José Antonio Quiñonero gris
# Fecha de creación: 12 de abril de 2022
# _____________________________________________________________________________

import numpy as np
import matplotlib.pyplot as plt

from config import *

# Parse command-line arguments and set up data directory
parse_args(description="Plot eigenstates and potential for NH3/ND3 double well")

plt.style.use(STYLE_FILE)

# *****************************************************************************
# INICIO
# *****************************************************************************


x, V = np.loadtxt(data("out-potencial_cm-1.dat"), unpack=True, skiprows=2)
n, Nconver, Econver, E = np.loadtxt(data("out-conver_energias_cm-1.dat"), unpack=True, skiprows=1)
x, Phi0, Phi2, Phi4 = np.loadtxt(data("out-funciones_pares_A.dat"), unpack=True, skiprows=2)
x, Phi1, Phi3, Phi5 = np.loadtxt(data("out-funciones_impares_A.dat"), unpack=True, skiprows=2)
x, dPhi0, dPhi2, dPhi4 = np.loadtxt(data("out-densidad_prob_pares_A.dat"), unpack=True, skiprows=2)
x, dPhi1, dPhi3, dPhi5 = np.loadtxt(data("out-densidad_prob_impares_A.dat"), unpack=True, skiprows=2)

def x1(n):
    res = np.sqrt(np.sqrt(E[n]*VB)/VB+1)*XE
    return res
def x2(n):
    res = np.sqrt(1-np.sqrt(E[n]*VB)/VB)*XE
    return res

# print(x1(0), x2(0))

# GRAFICA
nombre_grafica = 'funciones_y_potencial.pdf'
multiplicador = 200

# xmax = 1
# xmin = -xmax
# ymax = 3
# ymin = -ymax

xmax = 0.75
xmin = -xmax
ymax = 2500
ymin = 0

# width as measured in inkscape
width = 15.922
width = 7.2 * 1.5
# height = width / 1.618
height = 4.45 * 2

fig, axs = plt.subplots(2,2, figsize=(width, height), sharey=True, sharex=True)

# ==========================================
ax = axs[0][0]
# ==========================================
ax.hlines(y=E[0], xmin=-x1(0), xmax=-x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[0], xmin= x1(0), xmax= x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin=-x1(1), xmax=-x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin= x1(1), xmax= x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin=-x1(2), xmax=-x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin= x1(2), xmax= x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin=-x1(3), xmax=-x2(3), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin= x1(3), xmax= x2(3), lw=1.0, ls='-', color='k')
ax.plot(x, V, color='gray', label=r'$V(x)$')
# ax.plot(x, (dPhi0*multiplicador)+E[0], label=r'$\left| \Phi_{0^+} \right|^2$')
ax.plot(x, ( Phi0*multiplicador)+E[0], label=r'$\left| \Phi_{0^+} \right>$')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.legend(loc='upper right')
ax.set(ylabel=r'$E\ (\mathrm{cm^{-1}})$')
# ax.text(x=-xe, y=-3.3, s=r'$-x_e$', fontsize=18, horizontalalignment='center', verticalalignment='center')
# ax.text(x=-0.9, y=2.9, s=r'$v=0$', fontsize=18, horizontalalignment='left', verticalalignment='top')

# ==========================================
ax = axs[0][1]
# ==========================================
ax.hlines(y=E[0], xmin=-x1(0), xmax=-x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[0], xmin= x1(0), xmax= x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin=-x1(1), xmax=-x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin= x1(1), xmax= x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin=-x1(2), xmax=-x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin= x1(2), xmax= x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin=-x1(3), xmax=-x2(3), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin= x1(3), xmax= x2(3), lw=1.0, ls='-', color='k')
ax.plot(x, V, color='gray', label=r'$V(x)$')
# ax.plot(x, (dPhi1*multiplicador)+E[1], label=r'$\left| \Phi_{0^-} \right|^2$')
ax.plot(x, ( Phi1*multiplicador)+E[1], label=r'$\left| \Phi_{0^-} \right>$')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.legend(loc='upper right')
# ax.text(x=-xe, y=-3.3, s=r'$-x_e$', fontsize=18, horizontalalignment='center', verticalalignment='center')
# ax.text(x=-0.9, y=2.9, s=r'$v=0$', fontsize=18, horizontalalignment='left', verticalalignment='top')

# ==========================================
ax = axs[1][0]
# ==========================================
ax.hlines(y=E[0], xmin=-x1(0), xmax=-x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[0], xmin= x1(0), xmax= x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin=-x1(1), xmax=-x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin= x1(1), xmax= x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin=-x1(2), xmax=-x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin= x1(2), xmax= x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin=-x1(3), xmax=-x2(3), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin= x1(3), xmax= x2(3), lw=1.0, ls='-', color='k')
ax.plot(x, V, color='gray', label=r'$V(x)$')
# ax.plot(x, (dPhi2*multiplicador)+E[2], label=r'$\left| \Phi_{1^+} \right|^2$')
ax.plot(x, ( Phi2*multiplicador)+E[2], label=r'$\left| \Phi_{1^+} \right>$')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.legend(loc='upper right')
ax.set(xlabel=r'$x\ (\AA)$', ylabel=r'$E\ (\mathrm{cm^{-1}})$')
# ax.text(x=-xe, y=-3.3, s=r'$-x_e$', fontsize=18, horizontalalignment='center', verticalalignment='center')
# ax.text(x=-0.9, y=2.9, s=r'$v=0$', fontsize=18, horizontalalignment='left', verticalalignment='top')

# ==========================================
ax = axs[1][1]
# ==========================================
ax.hlines(y=E[0], xmin=-x1(0), xmax=-x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[0], xmin= x1(0), xmax= x2(0), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin=-x1(1), xmax=-x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[1], xmin= x1(1), xmax= x2(1), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin=-x1(2), xmax=-x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[2], xmin= x1(2), xmax= x2(2), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin=-x1(3), xmax=-x2(3), lw=1.0, ls='-', color='k')
ax.hlines(y=E[3], xmin= x1(3), xmax= x2(3), lw=1.0, ls='-', color='k')
ax.plot(x, V, color='gray', label=r'$V(x)$')
# ax.plot(x, (dPhi3*multiplicador)+E[3], label=r'$\left| \Phi_{1^-} \right|^2$')
ax.plot(x, ( Phi3*multiplicador)+E[3], label=r'$\left| \Phi_{1^+} \right>$')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.legend(loc='upper right')
ax.set(xlabel=r'$x\ (\AA)$')
# ax.text(x=-xe, y=-3.3, s=r'$-x_e$', fontsize=18, horizontalalignment='center', verticalalignment='center')
# ax.text(x=-0.9, y=2.9, s=r'$v=0$', fontsize=18, horizontalalignment='left', verticalalignment='top')

plt.savefig(nombre_grafica, transparent='True', bbox_inches='tight')
# plt.show()
