import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from impedance.visualization import plot_nyquist, plot_bode

# The following helper function are modified variants of those implement in impedance.py to enable the meaningful
# plotting of SPEIS data


def plot_speis_nyquist(ax, z, scale=1, units='Ohms', fmt='.-', cutoff=None, **kwargs):
    #Generate colormap
    colors = plt.cm.get_cmap('RdYlGn')
    if cutoff == None:
        cutoff = len(z)

    #Plot each point
    for i in range(len(z)):
        ax.plot(z[i][:cutoff].real, -z[i][:cutoff].imag, fmt, color=colors(i/len(z)), **kwargs)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$Z^{\prime}(\omega)$ ' +
                  '$[{}]$'.format(units), fontsize=20)
    ax.set_ylabel(r'$-Z^{\prime\prime}(\omega)$ ' +
                  '$[{}]$'.format(units), fontsize=20)
    ax.locator_params(axis='x', nbins=5, tight=True)
    ax.locator_params(axis='y', nbins=5, tight=True)
    ax.grid(b=True, which='major', axis='both', alpha=.5)
    limits = -np.log10(scale)
    if limits != 0:
        ax.ticklabel_format(style='sci', axis='both',
                            scilimits=(limits, limits))
    y_offset = ax.yaxis.get_offset_text()
    y_offset.set_size(18)
    t = ax.xaxis.get_offset_text()
    t.set_size(18)
    return ax


def plot_speis_bode(axes, f, z, scale=1, units='Ohms', fmt='.-', **kwargs):
    #Generate colormap
    colors = plt.cm.get_cmap('RdYlGn')
    ax_mag, ax_phs = axes
    for i in range(len(z)):
        ax_mag.plot(f[i], np.abs(z[i]), fmt, color=colors(i/len(z)), **kwargs)
        ax_phs.plot(f[i], -np.angle(z[i], deg=True), fmt, color=colors(i/len(z)), **kwargs)
    # ax_mag.plot(f, np.abs(z), fmt, **kwargs)
    # ax_phs.plot(f, -np.angle(z, deg=True), fmt, **kwargs)
    ax_mag.set_ylabel(r'$|Z(\omega)|$ ' +
                      '$[{}]$'.format(units), fontsize=20)
    ax_phs.set_ylabel(r'$-\phi_Z(\omega)$ ' + r'$[^o]$', fontsize=20)
    for ax in axes:
        # Set the frequency axes title and make log scale
        ax.set_xlabel('f [Hz]', fontsize=20)
        ax.set_xscale('log')

        # Make the tick labels larger
        ax.tick_params(axis='both', which='major', labelsize=14)

        # Change the number of labels on each axis to five
        ax.locator_params(axis='y', nbins=5, tight=True)

        # Add a light grid
        ax.grid(b=True, which='major', axis='both', alpha=.5)
    limits = -np.log10(scale)
    if limits != 0:
        ax_mag.ticklabel_format(style='sci', axis='y',
                                scilimits=(limits, limits))
    y_offset = ax_mag.yaxis.get_offset_text()
    y_offset.set_size(18)
    return axes

#Quick function to generate overview of the dataset with bode and nyquist plot
def plot_speis_overview(f, z):
    fig = plt.figure(constrained_layout=True, figsize=(12,5))
    gs = fig.add_gridspec(2, 2)
    f_ax1 = fig.add_subplot(gs[:, 0])
    f_ax1.set_title("Nyquist plot")
    f_ax2 = fig.add_subplot(gs[0, 1])
    f_ax2.set_title("Bode plot")
    f_ax3 = fig.add_subplot(gs[1, 1])
    plot_speis_nyquist(f_ax1, z)
    plot_speis_bode((f_ax2, f_ax3), f, z)
    return gs
    
def plot_model_fit_overview(f_i, z_i, model):
    #Generate plot data from fitted model
    z_fit = model.predict(f_i)

    fig = plt.figure(constrained_layout=True, figsize=(12,5))
    gs = fig.add_gridspec(2, 2)
    f_ax1 = fig.add_subplot(gs[:, 0])
    f_ax1.set_title("Nyquist plot")
    f_ax2 = fig.add_subplot(gs[0, 1])
    f_ax2.set_title("Bode plot")
    f_ax3 = fig.add_subplot(gs[1, 1])
    plot_nyquist(f_ax1, z_i, fmt='o')
    plot_nyquist(f_ax1, z_fit, fmt='-')
    plot_bode((f_ax2, f_ax3), f_i, z_i, ls='', marker='s', label='Data')
    plot_bode((f_ax2, f_ax3), f_i, z_fit, ls='-', marker='', label='Fit')
    f_ax2.legend()
    return gs
