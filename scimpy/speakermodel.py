# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:59 2016

@author: showard
"""

import numpy as np
import matplotlib.ticker
# import matplotlib.pyplot as plt
import scipy.optimize


def cheby_a1(k):
    """Calculate A1 of a Chebyshev filter from k"""
    return 2.6131*k/(.125*k**4+.75*k**2+.125)**(.25)


def cheby_a2(k):
    """Calculate A2 of a Chebyshev filter from k"""
    return (2.4143*k**2+1)/(.125*k**4+.75*k**2+.125)**(.5)


def cheby_a3(k):
    """Calculate A3 of a Chebyshev filter from k"""
    return (0.9239*k**3+1.6892*k)/(.125*k**4+.75*k**2+.125)**(.75)


def cheby_qts(k):
    """Calculate Qts of a Chebyshev filter for a given k"""
    return 1/np.sqrt(cheby_a1(k)*cheby_a3(k))


def cheby_find_k(qts):
    """Find the Chebyshev k for a given speaker driver Qts"""
    return scipy.optimize.fsolve(lambda k: qts-cheby_qts(k), 1)


def find_alpha(k):
    """Find compresion ratio alpha (Vas/Vb) for a C4 box given k"""
    return ((
        cheby_a1(k)*cheby_a2(k)*cheby_a3(k)-cheby_a1(k)**2-cheby_a3(k)**2) /
            cheby_a3(k)**2)[0]


def find_ported_params_c4(qts):
    """Find compresion ratio alpha (Vas/Vb) and normalized box frequency
    (fb/fs) for a C4 box given qts"""
    k = cheby_find_k(qts)
    alpha = find_alpha(k)
    h__ = (cheby_a1(k)/cheby_a3(k))[0]
    return alpha, h__


def find_ported_params_qb3(qts):
    """Find compresion ratio alpha (Vas/Vb) and normalized box frequency
    (fb/fs) for a QB3 box given qts"""
    k = cheby_find_k(qts)
    alpha = find_alpha(k)
    h__ = 1/(qts*np.sqrt(8-8*qts**2))
    qb3_a2 = 1/(2*qts**2*h__)
    qb3_a1 = (2+qb3_a2**2)/(2*np.sqrt(2*qb3_a2))
    qb3_a3 = np.sqrt(2*qb3_a2)
    alpha = (qb3_a1*qb3_a2*qb3_a3-qb3_a1**2-qb3_a3**2)/qb3_a3**2
    print(alpha, h__)
    return alpha, h__


def sealed_find_vb_qt_func(optimization_vars, vas, fs_, f3_, qts):
    """Function used with scipy optimization fsolve function to find Qt and Vb
    for a desired 3dB cut-off frequency (F3) when given a driver Qts"""
    qt_ = optimization_vars[0]
    vb_ = optimization_vars[1]
#    vas = args[0]
#    fs=args[1]
#    f3=args[2]
#    qts=args[3]
    fc_ = fs_*np.sqrt(vas/vb_+1)
    out = [0, 0]
    out[0] = fc_*np.sqrt((1/qt_**2-2+np.sqrt((2-1/qt_**2)**2+4))/2)-f3_
    out[1] = ((1-(qts/qt_)**2)/(qts/qt_)**2)-vas/vb_
    return out


def sealed_find_vb_qt(vas, fs_, f3_, qts):
    """Find Qt and Vbox for a desired 3dB cut-off frequency (F3) and driver
    Qts"""
    return scipy.optimize.fsolve(sealed_find_vb_qt_func,
                                 [qts, vas],
                                 args=(vas, fs_, f3_, qts))


def plot_impedance(ax1, ax2, freqs, magnitude, phase):
    ax1.plot(freqs, magnitude, 'b-')
    ax2.plot(freqs, phase, 'r--')

    ax1.set_ylabel('Impedance Magnitude (Ohms)', color='b')
    ax1.set_title('Impedance Magnitude and Phase versus Frequency')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)', color='r')
    ax1.set_xscale('log')
    ax2.set_xscale('log')
    ax1.set_xlim([20, 20000])

    ax1.grid(True, which="both", color="0.65", ls='-')
    ax2.grid(True, which="both", color="0.65", ls='-')
    ax1.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    for tlabel in ax1.get_yticklabels():
        tlabel.set_color('b')
    for tlabel in ax2.get_yticklabels():
        tlabel.set_color('r')
    ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(11))
    ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(11))


def calc_impedance(plotwidget,
                   re_,
                   le_,
                   n_,
                   cms,
                   mms,
                   rms,
                   sd_,
                   bl_,
                   vb_=np.inf,
                   l_over_a=np.inf):
    """Calculate and plot imedpance magnitude, impedance phase, SPL magnitude,
    acoustic output phase, and acoustic output group delay"""
    # omegas = 1/math.sqrt(cms*mms)
    res = bl_**2/rms
    les = bl_**2*cms
    ces = mms/bl_**2
    leb = bl_**2/sd_**2*vb_/(1.18*345**2)
    cev = sd_**2/bl_**2*1.18*l_over_a
    # qes = omegas*res*ces
    omega = np.logspace(1.3, 4.3, 1000)*2*np.pi
    zvc = le_*(omega*1j)**n_
    re_ = re_ + zvc.real  # freq. dependent resistance
    le_ = zvc.imag/omega  # freq. dependent inductance
    yacoustic = -1j / (leb * omega-1/(omega*cev))  # Ya = 1/ Za
    zmech = (1/res+1/(omega*les*1j)+omega*ces*1j + yacoustic)**(-1)
    ztotal = zmech+re_+1j*omega*le_

    transferfunc = 1j*(omega*zmech/ztotal)*re_*ces
    print(l_over_a)
    if l_over_a != np.inf:
        transferfunc = transferfunc*(1j*omega*leb) / \
            (1j*omega*leb+1/(1j*omega*cev))

    plotwidget.clear_axes()  # at some point we can keep the hold on
    plot_impedance(ax1=plotwidget.axes1,
                   ax2=plotwidget.axes1b,
                   freqs=omega/2/np.pi,
                   magnitude=abs(ztotal),
                   phase=np.angle(ztotal)*180/np.pi)

    ax_power = plotwidget.axes2
    efficiency = (sd_**2 * 1.18/345/2/np.pi/re_/ces**2/bl_**2) * \
        abs(transferfunc)**2
    power_spl = 112.1+10 * np.log10(efficiency)
    ax_power.plot(omega/2/np.pi, power_spl, 'b-')

    # For now, just show group delay, possibly more interesting to people?
    # ax_phase = fig2.add_subplot(312)
    # ax_phase = plotwidget.axes4
    # ax_phase = ax_power.twinx()
    # ax_phase.plot(omega/2/np.pi, np.angle(transferfunc)*180/np.pi)

    # TODO impulse response instead of phase?
    # response = sum(SPL_mag*cos(omega*t+spl_phase)*delta_omega) acounts for
    # non-linear FRD files and data (logrithmic) and FFT (linear)
    ax_groupdelay = plotwidget.axes2b
    ax_groupdelay.plot(omega/2/np.pi,
                       -np.gradient(np.unwrap(
                           np.angle(transferfunc)))/np.gradient(omega)*1000,
                       'r--')
    ax_power.set_title('Speaker Performance')
    ax_power.set_ylabel('SPL (dB 1W1m)', color='b')
    # ax_phase.set_ylabel('Phase (degrees)')
    ax_groupdelay.set_ylabel('Group Delay (ms)', color='r')
    ax_power.set_xlabel('Frequency (Hz)')
    ax_power.set_xscale('log')
    ax_power.set_xlim([20, 20000])
    ax_power.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter("%d"))
    # ax_phase.set_xscale('log')
    # ax_phase.xaxis.set_major_formatter(
    #     matplotlib.ticker.FormatStrFormatter("%d"))
    ax_groupdelay.set_xscale('log')
    ax_groupdelay.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter("%d"))
    ax_power.grid(True, which="both", color="0.65", ls='-')
    # ax_phase.grid(True, which="both", color="0.65", ls='-')
    ax_groupdelay.grid(True, which="both", color="0.65", ls='-')
    for tlabel in ax_power.get_yticklabels():
        tlabel.set_color('b')
    for tlabel in ax_groupdelay.get_yticklabels():
        tlabel.set_color('r')
    # align_y_axis(ax_power, ax_groupdelay, 9)

    ax_power.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(11))
    ax_groupdelay.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(11))

    #ax_power.set_ylim([min(ax_power.get_yticks()), max(ax_power.get_yticks())])
    #ax_groupdelay.set_ylim([min(ax_groupdelay.get_yticks()), max(ax_groupdelay.get_yticks())])
    # fig2.show()
    plotwidget.draw()
