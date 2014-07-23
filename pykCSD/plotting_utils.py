# -*- coding: utf-8 -*-
from matplotlib import pylab as plt
from mpl_toolkits.mplot3d import Axes3D

"""
Simple plotting routines for KCSD 1D, 2D, 3D.
"""


# TODO: ADD COLORBARS
def plot_1D(elec_pos, meas_pots, est_pots, est_csd, extent):
    """
    Describe what is plotted
    """
    fig, (ax11, ax12, ax13) = plt.subplots(1, 3, sharex=True)

    ax11.scatter(elec_pos, meas_pots)
    ax11.set_title('Measured potentials')

    ax12.plot(extent, est_pots)
    ax12.set_title('Calculated potentials')

    ax13.plot(extent, est_csd)
    ax13.set_title('Calculated CSD')
    plt.show()


def plot_2D(elec_pos, meas_pots, est_pots, est_csd, extent):
    """
    Describe what is plotted
    """
    fig, (ax11, ax12, ax13) = plt.subplots(1, 3)

    ax11.set_xlim([extent[0], extent[1]])
    ax11.set_ylim([extent[2], extent[3]])
    ax11.scatter(x=elec_pos[:, 0], y=elec_pos[:, 1],
                 c=meas_pots, s=200, marker='s')
    ax11.set_title('Measured potentials')

    ax12.imshow(est_pots.T, interpolation='none',
                extent=extent, aspect="auto", origin='lower')
    ax12.set_title('Calculated potentials')
    ax12.autoscale_view(True, True, True)

    ax13.imshow(est_csd.T, interpolation='none',
                extent=extent, aspect="auto", origin='lower')
    ax13.set_title('Calculated CSD')
    ax13.autoscale_view(True, True, True)

    plt.show()


def plot_3D(elec_pos, est_pots, est_csd, extent):
    """
    Describe what is plotted
    """
    extent_x = extent[:4]
    extent_y = extent[2:6]
    extent_z = [extent[4], extent[5], extent[0], extent[1]]

    fig = plt.figure()

    ax11 = fig.add_subplot(2, 4, 1, projection='3d')
    ax11.set_title('Electrode setup')
    ax11.scatter(elec_pos[:, 0], elec_pos[:, 1], elec_pos[:, 2])

    ax12 = fig.add_subplot(2, 4, 2)
    ax12.imshow(est_pots[0, :, :].T, interpolation='none',
                extent=extent_x, aspect="auto", origin='lower')
    ax12.set_title('Calculated potentials [0-axis]')
    ax12.autoscale_view(True, True, True)

    ax13 = fig.add_subplot(2, 4, 3)
    ax13.imshow(est_pots[:, 0, :].T, interpolation='none',
                extent=extent_y, aspect="auto", origin='lower')
    ax13.set_title('Calculated potentials [1-axis]')
    ax13.autoscale_view(True, True, True)

    ax14 = fig.add_subplot(2, 4, 4)
    ax14.imshow(est_pots[:, :, 0].T, interpolation='none',
                extent=extent_z, aspect="auto", origin='lower')
    ax14.set_title('Calculated potentials [2-axis]')
    ax14.autoscale_view(True, True, True)

    ax22 = fig.add_subplot(2, 4, 6)
    ax22.imshow(est_csd[0, :, :].T, interpolation='none',
                extent=extent_x, aspect="auto", origin='lower')
    ax22.set_title('Calculated CSD [0-axis]')
    ax22.autoscale_view(True, True, True)

    ax23 = fig.add_subplot(2, 4, 7)
    ax23.imshow(est_csd[:, 0, :].T, interpolation='none',
                extent=extent_y, aspect="auto", origin='lower')
    ax23.set_title('Calculated CSD [1-axis]')
    ax23.autoscale_view(True, True, True)

    ax24 = fig.add_subplot(2, 4, 8)
    ax24.imshow(est_csd[:, :, 0].T, interpolation='none',
                extent=extent_z, aspect="auto", origin='lower')
    ax24.set_title('Calculated CSD [2-axis]')
    ax24.autoscale_view(True, True, True)

    plt.show()


def plot_comparison_1D(X, elec_pos, true_csd, true_pots, rec_csd, rec_pots, err_csd, err_pot):
    """
    Describe what is plotted
    """
    fig = plt.figure()

    ax11 = fig.add_subplot(2, 3, 1)
    ax11.plot(X, true_csd)
    ax11.set_title('True CSD')

    ax12 = fig.add_subplot(2, 3, 2)
    ax12.plot(X, rec_csd)
    ax12.set_title('Reconstructed CSD')

    ax13 = fig.add_subplot(2, 3, 3)
    ax13.plot(X, err_csd)
    ax13.set_title('CSD reconstruction error')

    ax21 = fig.add_subplot(2, 3, 4)
    ax21.plot(X, true_pots)
    ax21.set_title('True LFP (forward scheme calculation from CSD)')

    ax22 = fig.add_subplot(2, 3, 5)
    ax22.plot(X, rec_pots)
    ax22.scatter(elec_pos, [0.1]*len(elec_pos))
    ax22.set_title('Reconstructed LFP')

    ax23 = fig.add_subplot(2, 3, 6)
    ax23.plot(X, err_pot)
    ax23.set_title('LFP econstruction Error')

    plt.show()


def plot_comparison_2D(X, Y, elec_pos, true_csd, true_pots, rec_csd, rec_pots, err_csd, err_pot):
    """
    Describe what is plotted
    """
    fig = plt.figure()

    ax11 = fig.add_subplot(2, 3, 1)
    plt.pcolor(X, Y, true_csd)
    ax11.set_title('True CSD')

    ax12 = fig.add_subplot(2, 3, 2)
    plt.pcolor(X, Y, rec_csd)
    ax12.set_title('Reconstructed CSD')
    """
    ax13 = fig.add_subplot(2, 3, 3)
    ax13.plot(X, err_csd)
    ax13.set_title('CSD reconstruction error')
    """
    ax21 = fig.add_subplot(2, 3, 4)
    plt.pcolor(X,Y,true_pots)
    ax21.set_title('True LFP (forward scheme calculation from CSD)')

    ax22 = fig.add_subplot(2, 3, 5)
    plt.pcolor(X, Y, rec_pots)
    ax22.scatter(elec_pos[:,0], elec_pos[:,1],marker='o',c='b',s=5,zorder=10)
    #ax22.scatter(elec_pos, [0.1]*len(elec_pos))
    ax22.set_title('Reconstructed LFP')
    """
    ax23 = fig.add_subplot(2, 3, 6)
    ax23.plot(X, err_pot)
    ax23.set_title('LFP econstruction Error')"""

    plt.show()