import numpy as np
import matplotlib.pyplot as plt

# The following helper function are modified variants of those implement in impedance.py to enable the meaningful
# plotting of SPEIS data


def plot_speis_nyquist(ax, z, scale=1, units='Ohms', fmt='.-', **kwargs):
    #Generate colormap
    colors = plt.cm.get_cmap('RdYlGn')

    #Plot each point
    for i in range(len(z)):
        ax.plot(z[i].real, -z[i].imag, fmt, color=colors(i/len(z)), **kwargs)
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

# %TODO: Quick function to generate overview of the dataset with bode and nyquist plot
# def plot_speis_overview(f, z):
#     fig_overview, axs_overview = plt.subplots(ncols=2, nrows=2)
#     fig_nyq, ax_nyq = plt.subplots()
#     fig_bode, ax_bode = plt.subplots(nrows=2, figsize=(5, 5))
#     ax_nyq = plot_speis_nyquist(ax_nyq, z)
#     ax_bode = plot_speis_bode(ax_bode, f, z)
#
#     axs_overview[0, 2]
#     gs = axs_overview[1, 2].get_gridspec()
#     for ax in axs_overview[1:, -1]:
#         ax.remove()
#     axbig = fig.add_subplot(gs[1:, -1])
#     plt.show()
