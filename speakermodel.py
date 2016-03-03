# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:59 2016

@author: showard
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def calc_impedance(re, le, cms, mms, rms, sd, bl):
    omegas = 1/math.sqrt(cms*mms)
    res = bl**2/rms
    les = bl**2*cms
    ces = mms/bl**2
    qes = omegas*res*ces
    omega = np.logspace(1.3, 4.3, 10000)*2*np.pi
    Zm = (1/res+1/(omega*les*1j)+omega*ces*1j)**(-1)
    Z = Zm+re+omega*le*1j

    transferfunc = 1j*(omega*Zm/Z)*re*ces  # TODO need to remove RE and Les that were pullsed out! maybe even correct text?

    fig = plt.figure()
    ax = fig.add_subplot(211)

    ax.plot(omega/2/np.pi, abs(Z))
    ax2 = fig.add_subplot(212)
    ax2.plot(omega/2/np.pi, np.angle(Z)*180/np.pi)
    ax.set_ylabel('Impedance Magnitude (Ohms)')
    ax.set_title('Impedance Magnitude and Phase versus Frequency')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax.set_xscale('log')
    ax2.set_xscale('log')
    ax.grid()
    ax2.grid()
    fig.show()

    fig2 = plt.figure()
    ax_power = fig2.add_subplot(311)
    efficiency = (sd**2 * 1.18/345/2/np.pi/re/ces**2/bl**2) * abs(transferfunc)**2  # W WRONG EQUATION
    power_spl = 112.1+10 * np.log10(efficiency)
    ax_power.plot(omega/2/np.pi, power_spl)
    ax_phase = fig2.add_subplot(312)
    ax_phase.plot(omega/2/np.pi, np.angle(transferfunc)*180/np.pi)
    ax_groupdelay = fig2.add_subplot(313)
    ax_groupdelay.plot(
        omega/2/np.pi,
        -np.gradient(np.angle(transferfunc))/np.gradient(omega)*1000)
    ax_power.set_title('Infinite Baffle Performance')
    ax_power.set_ylabel('SPL (dB 1W1m)')
    ax_phase.set_ylabel('Phase (degrees)')
    ax_groupdelay.set_ylabel('Group Delay (ms)')
    ax_groupdelay.set_xlabel('Frequency (Hz)')
    ax_power.set_xscale('log')
    #ax_power.set_yscale('log')
    ax_phase.set_xscale('log')
    ax_groupdelay.set_xscale('log')
    ax_power.grid()
    ax_phase.grid()
    ax_groupdelay.grid()
    fig2.show()
