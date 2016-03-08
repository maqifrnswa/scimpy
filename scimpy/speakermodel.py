# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:59 2016

@author: showard
"""

import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
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


def find_sealed_params(qts):
    """Find compresion ratio alpha (Vas/Vb) and normalized box frequency
    (fb/fs) for a C4 box given k"""
    k = cheby_find_k(qts)
    alpha = find_alpha(k)
    h__ = (cheby_a1(k)/cheby_a3(k))[0]
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


def calc_impedance(re_,
                   le_,
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
    omega = np.logspace(1.3, 4.3, 10000)*2*np.pi
    yacoustic = -1j / (leb * omega-1/(omega*cev))  # Ya = 1/ Za
    zmech = (1/res+1/(omega*les*1j)+omega*ces*1j + yacoustic)**(-1)
    ztotal = zmech+re_+omega*le_*1j

    transferfunc = 1j*(omega*zmech/ztotal)*re_*ces
    print(l_over_a)
    if l_over_a != np.inf:
        transferfunc = transferfunc*(1j*omega*leb) / \
            (1j*omega*leb+1/(1j*omega*cev))

    plt.ion()
    fig = plt.figure()
    ax1 = fig.add_subplot(211)

    ax1.plot(omega/2/np.pi, abs(ztotal))
    ax2 = fig.add_subplot(212)
    ax2.plot(omega/2/np.pi, np.angle(ztotal)*180/np.pi)
    ax1.set_ylabel('Impedance Magnitude (Ohms)')
    ax1.set_title('Impedance Magnitude and Phase versus Frequency')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax1.set_xscale('log')
    ax2.set_xscale('log')
    ax1.grid(True, which="both", ls=":")  # ,color="0.65")
    ax2.grid(True, which="both", ls=":")  # ,color="0.65")
    ax1.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    fig.show()

    fig2 = plt.figure()
    ax_power = fig2.add_subplot(311)
    efficiency = (sd_**2 * 1.18/345/2/np.pi/re_/ces**2/bl_**2) * \
        abs(transferfunc)**2
    power_spl = 112.1+10 * np.log10(efficiency)
    ax_power.plot(omega/2/np.pi, power_spl)
    ax_phase = fig2.add_subplot(312)
    ax_phase.plot(omega/2/np.pi, np.angle(transferfunc)*180/np.pi)
    ax_groupdelay = fig2.add_subplot(313)
    ax_groupdelay.plot(omega/2/np.pi,
                       -np.gradient(np.unwrap(
                           np.angle(transferfunc)))/np.gradient(omega)*1000)
    ax_power.set_title('Speaker Performance')
    ax_power.set_ylabel('SPL (dB 1W1m)')
    ax_phase.set_ylabel('Phase (degrees)')
    ax_groupdelay.set_ylabel('Group Delay (ms)')
    ax_groupdelay.set_xlabel('Frequency (Hz)')
    ax_power.set_xscale('log')
    ax_power.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter("%d"))
    # ax_power.set_yscale('log')
    ax_phase.set_xscale('log')
    ax_phase.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter("%d"))
    ax_groupdelay.set_xscale('log')
    ax_groupdelay.xaxis.set_major_formatter(
        matplotlib.ticker.FormatStrFormatter("%d"))
    ax_power.grid(True, which="both", ls=":")  # ,color="0.65")
    ax_phase.grid(True, which="both", ls=":")  # ,color="0.65")
    ax_groupdelay.grid(True, which="both", ls=":")  # ,color="0.65")
    fig2.show()
