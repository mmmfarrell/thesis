import numpy as np
from math import *
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
from scipy.io import loadmat

np.set_printoptions(linewidth=150)
plt.rc('text', usetex=True)
#  plt.rc('font', family='serif')
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('axes', labelsize=10)

# Width /height of final product
#  width = 3.487
width = 6.5
#  height = width / 1.618
height = width / 1.9
#  height = width * 1.618
#  height = width * 1.25

# SIM FIG 8
data = loadmat('sim_fig8.mat')
t = data['t']
x = data['x']
xc = data['xc']

ylabel = [r'$ \mathrm{\mathbf{e}}_1^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_2^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_3^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)']

f, axes = plt.subplots(3, 1, sharex=True, figsize=(width,height))
f.subplots_adjust(left=.1, bottom=.12, right=.97, top=.90)

for i in range(3):
    ax = axes[i]
    l1 = ax.plot(t[0,:], x[i,:], label=r"$\hat{x}")
    l2 = ax.plot(t[0,:], xc[i,:], 'r--', label=r"$\check{x}$")

    if i == 0:
        ax.set_ylim((-5., 5.))
    elif i == 1:
        ax.set_ylim((-3., 3.))
    elif i == 2:
        ax.set_ylim((-10., 0.))

    ax.set_ylabel(ylabel[i])
    ax.set_xlim((0., 20.))
    ax.grid(True)
f.legend((l1[0], l2[0]), (r"$\hat{x}$", r"$\check{x}$"), loc="upper center",
        ncol=3)

ax.set_xlabel("Time (s)")
f.savefig('plots/sim_fig8_position.pdf')

# SIM WAYPOINTS
data = loadmat('sim_wps.mat')
t = data['t']
x = data['x']
xc = data['xc']

ylabel = [r'$ \mathrm{\mathbf{e}}_1^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_2^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_3^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)']

f, axes = plt.subplots(3, 1, sharex=True, figsize=(width,height))
f.subplots_adjust(left=.1, bottom=.12, right=.97, top=.90)

for i in range(3):
    ax = axes[i]
    l1 = ax.plot(t[0,:], x[i,:], label=r"$\hat{x}")
    l2 = ax.plot(t[0,:], xc[i,:], 'r--', label=r"$\check{x}$")

    if i == 0:
        ax.set_ylim((-5., 5.))
    elif i == 1:
        ax.set_ylim((-3., 3.))
    elif i == 2:
        ax.set_ylim((-10., 0.))

    ax.set_ylabel(ylabel[i])
    ax.set_xlim((0., 70.))
    ax.grid(True)
f.legend((l1[0], l2[0]), (r"$\hat{x}$", r"$\check{x}$"), loc="upper center",
        ncol=3)

ax.set_xlabel("Time (s)")
f.savefig('plots/sim_wps_position.pdf')

# HARDWARE WAYPOINTS
data = loadmat('mocap_updown_wps.mat')
t = data['t']
x = data['x']
xc = data['xc']

ylabel = [r'$ \mathrm{\mathbf{e}}_1^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_2^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_3^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)']

f, axes = plt.subplots(3, 1, sharex=True, figsize=(width,height))
f.subplots_adjust(left=.1, bottom=.12, right=.97, top=.90)

for i in range(3):
    ax = axes[i]
    l1 = ax.plot(t[0,:], x[i,:], label=r"$\hat{x}")
    l2 = ax.plot(t[0,:], xc[i,:], 'r--', label=r"$\check{x}$")

    if i == 0:
        ax.set_ylim((-1., 1.))
    elif i == 1:
        ax.set_ylim((-2., 2.))
    elif i == 2:
        ax.set_ylim((-3., 0.))

    ax.set_ylabel(ylabel[i])
    ax.set_xlim((0., 70.))
    ax.grid(True)
f.legend((l1[0], l2[0]), (r"$\hat{x}$", r"$\check{x}$"), loc="upper center",
        ncol=3)

ax.set_xlabel("Time (s)")
f.savefig('plots/mocap_wps_position.pdf')

# HARDWARE FIG8
data = loadmat('mocap_updown_fig8.mat')
t = data['t']
x = data['x']
xc = data['xc']

ylabel = [r'$ \mathrm{\mathbf{e}}_1^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_2^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)',
            r'$ \mathrm{\mathbf{e}}_3^{\mathsf{T}} \mathrm{\mathbf{p}}_{b/I}^I $ (m)']

f, axes = plt.subplots(3, 1, sharex=True, figsize=(width,height))
f.subplots_adjust(left=.1, bottom=.12, right=.97, top=.90)

for i in range(3):
    ax = axes[i]
    l1 = ax.plot(t[0,:], x[i,:], label=r"$\hat{x}")
    l2 = ax.plot(t[0,:], xc[i,:], 'r--', label=r"$\check{x}$")

    if i == 0:
        ax.set_ylim((-1., 1.))
    elif i == 1:
        ax.set_ylim((-2., 2.))
    elif i == 2:
        ax.set_ylim((-3., 0.))

    ax.set_ylabel(ylabel[i])
    ax.set_xlim((0., 60.))
    ax.grid(True)
f.legend((l1[0], l2[0]), (r"$\hat{x}$", r"$\check{x}$"), loc="upper center",
        ncol=3)

ax.set_xlabel("Time (s)")
f.savefig('plots/mocap_fig8_position.pdf')

# HARDWARE FIG8 top-down view
#  f = plt.figure(figsize=(width, height))
f, axes = plt.subplots(1, 1, figsize=(width, height))
f.subplots_adjust(left=.1, bottom=.13, right=.97, top=.90)
l1 = plt.plot(x[1,:], x[0,:])
l2 = plt.plot(xc[1,:], xc[0,:], 'r-')
plt.grid(True)
plt.xlim(-1.1, 1.1)
plt.ylim(-0.6, 0.6)
plt.xlabel(ylabel[1])
plt.ylabel(ylabel[0])
f.legend((l1[0], l2[0]), (r"$\hat{x}$", r"$\check{x}$"), loc="upper center",
        ncol=3)

f.savefig('plots/mocap_fig8_position_2d.pdf')
