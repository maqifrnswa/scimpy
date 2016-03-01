# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:59 2016

@author: showard
"""

import numpy
import matplotlib.pyplot as plt

def calcImpedance(re,le,cms,mms,res,sd,bl):
    les=bl**2*cms
    ces=mms/bl**2
    omega=numpy.logspace(1.3,4.3,10000)*2*numpy.pi
    Zm=(1/res+1/(omega*les*1j)+omega*ces*1j)**(-1)
    Z=Zm+re+omega*le*1j

    transferfunc= omega*Zm/Z

    fig = plt.figure()
    ax = fig.add_subplot(211)

    ax.plot(omega/2/numpy.pi,
                 abs(Z))
    ax2 = fig.add_subplot(212)
    ax2.plot(omega/2/numpy.pi,
                 numpy.angle(Z)*180/numpy.pi)
    ax.set_ylabel('Impedance Magnitude (Ohms)')
    ax.set_title('Impedance Magnitude and Phase versus Frequency')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax.set_xscale('log')
    ax2.set_xscale('log')
    ax.grid()
    ax2.grid()
    fig.show()

    fig2=plt.figure()
    ax_power=fig2.add_subplot(311)
    ax_power.plot(omega/2/numpy.pi,abs(transferfunc)**2)
    ax_phase=fig2.add_subplot(312)
    ax_phase.plot(omega/2/numpy.pi,numpy.angle(transferfunc)*180/numpy.pi)
    ax_groupdelay=fig2.add_subplot(313)
    ax_groupdelay.plot(omega/2/numpy.pi,-numpy.gradient(numpy.angle(transferfunc))/numpy.gradient(omega)*1000)
    ax_power.set_title('Infinite Baffle Performance')
    ax_power.set_ylabel('SPL (dB) NOT YET')
    ax_phase.set_ylabel('Phase (degrees)')
    ax_groupdelay.set_ylabel('Group Delay (ms)')
    ax_groupdelay.set_xlabel('Frequency (Hz)')
    ax_power.set_xscale('log')
    ax_power.set_yscale('log')
    ax_phase.set_xscale('log')
    ax_groupdelay.set_xscale('log')
    ax_power.grid()
    ax_phase.grid()
    ax_groupdelay.grid()
    fig2.show()
