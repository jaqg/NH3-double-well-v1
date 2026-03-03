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

x, V                                 = np.loadtxt(data("out-potencial_cm-1.dat"), unpack=True, skiprows=2)
n, Nconver, Econ, E                  = np.loadtxt(data("out-conver_energias_cm-1.dat"),  unpack=True, skiprows=1)
alfa, E_alfa, pcx1, pcx2, pcx3, pcx4 = np.loadtxt(data("out-puntos_corte.dat"), unpack=True, skiprows=3)

#
#
def x1ee(n):
    res = np.sqrt(np.sqrt(E[n]*VB)/VB+1)*XE
    return res
def x2ee(n):
    res = np.sqrt(1-np.sqrt(E[n]*VB)/VB)*XE
    return res

def set_share_axes(axs, target=None, sharex=False, sharey=False):
    if target is None:
        target = axs.flat[0]
    # Manage share using grouper objects
    for ax in axs.flat:
        if sharex:
            # target._shared_x_axes.join(target, ax)
            target._shared_axes['x'].join(target, ax)
        if sharey:
            # target._shared_y_axes.join(target, ax)
            target._shared_axes['y'].join(target, ax)
    # Turn off x tick labels and offset text for all but the bottom row
    if sharex and axs.ndim > 1:
        for ax in axs[:-1,:].flat:
            ax.xaxis.set_tick_params(which='both', labelbottom=False, labeltop=False)
            ax.xaxis.offsetText.set_visible(False)
    # Turn off y tick labels and offset text for all but the left most column
    if sharey and axs.ndim > 1:
        for ax in axs[:,1:].flat:
            ax.yaxis.set_tick_params(which='both', labelleft=False, labelright=False)
            ax.yaxis.offsetText.set_visible(False)

#
# width as measured in inkscape
width = 15.922
width = 7.2 * 1.5
width = 5.4
# height = width / 1.618
height = 4.45
#
width = 8.268
height = 11.693
fig, axs = plt.subplots(4,2,figsize=(width, height))
# gridspec_kw={'height_ratios': [1, 1, 3]}
# wspace=0.1, hspace=0.1, left=0.1, right=0.4, bottom=0.1, top=0.9
set_share_axes(axs[:3,:], sharex=True, sharey=True)
set_share_axes(axs[:4,:1], sharex=True, sharey=True)

lista_alfa_4EE = [0, 15, 30, 45, 60, 75, 90]  # subfig uses 7 selected angles

# Lineas horizontales de energia
for i in range(4):
    for j in range(2):
        ax = axs[i][j]
        for l in range(4):
            ax.hlines(y=E[l], xmin=-x1ee(l), xmax=-x2ee(l), lw=1.0, ls='-', color='gray')
            ax.hlines(y=E[l], xmin= x1ee(l), xmax= x2ee(l), lw=1.0, ls='-', color='gray')
# ------------------------------------------------
nombre_grafica = 'paquetes_subfig.pdf'
xmax = 0.75
xmin = -xmax
ymax = 2500
ymin = 0
multiplicador=150
transparencia=0.5
# ------------------------------------------------
# Panel layout: left column rows 0-3, right column rows 0-2
panel_positions = [(0,0), (1,0), (2,0), (3,0), (0,1), (1,1), (2,1)]

for panel_idx, (row, col) in enumerate(panel_positions):
    ax = axs[row][col]
    alfa_4EE = lista_alfa_4EE[panel_idx]
    # look up pcx index for this alpha value in the puntos_corte data
    idx = list(alfa).index(alfa_4EE)
    x1 = pcx1[idx]
    x2 = pcx2[idx]
    x3 = pcx3[idx]
    x4 = pcx4[idx]
    alfa_malo, E_Psi, x, Psi, dPsi = np.loadtxt(data('out-psi_4EE_alfa={}.dat'.format(alfa_4EE)), unpack=True, skiprows=4)
    ax.hlines(y=E_Psi[0], xmin=x1, xmax=x2, lw=1.0, ls='-', color='k')
    ax.hlines(y=E_Psi[0], xmin=x3, xmax=x4, lw=1.0, ls='-', color='k')
    ax.plot(x, V, lw=1.3, color='gray')
    ax.plot(x, (dPsi*multiplicador) + E_Psi[0], label=r'$\left| \psi \right|^2$')
    ax.plot(x, (Psi*multiplicador) + E_Psi[0], label=r'$\left| \psi \right>$')
    # titles and labels
    title = r'$\alpha = {:.0f}^\circ$'.format(alfa_4EE)
    ax.set(title=title)
    if col == 0:
        ax.set(ylabel=r'$E\ (\mathrm{cm^{-1}})$')
    if row == 3:
        ax.set(xlabel=r'$x\ (\AA)$')
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.legend(loc='upper right')

# clear the unused 8th panel
ax = axs[3][1]
ax.clear()
ax.axis('off')

plt.savefig(nombre_grafica, transparent='True', bbox_inches='tight')
# plt.show()
