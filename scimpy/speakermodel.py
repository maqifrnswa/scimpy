# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:43:59 2016

@author: showard
"""

import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import scipy.optimize
import math

def chebyA1(k):
    return 2.6131*k/(.125*k**4+.75*k**2+.125)**(.25)
    
def chebyA2(k):
    return (2.4143*k**2+1)/(.125*k**4+.75*k**2+.125)**(.5)
    
def chebyA3(k):
    return (0.9239*k**3+1.6892*k)/(.125*k**4+.75*k**2+.125)**(.75)

def chebyQts(k):
    return 1/np.sqrt(chebyA1(k)*chebyA3(k))

def cheby_find_k(qts):
    return scipy.optimize.fsolve(lambda k: qts-chebyQts(k),1)

def find_alpha(k):
    return ((chebyA1(k)*chebyA2(k)*chebyA3(k)-chebyA1(k)**2-chebyA3(k)**2)/chebyA3(k)**2)[0]

def find_sealed_params(qts):
    k=cheby_find_k(qts)
    alpha = find_alpha(k)
    h = (chebyA1(k)/chebyA3(k))[0]
    return alpha, h
    
    
def sealed_find_vb_qt_func(x, vas, fs, f3, qts): 
    qt = x[0]
    vb = x[1]
#    vas = args[0]
#    fs=args[1]
#    f3=args[2]
#    qts=args[3]
    fc = fs*np.sqrt(vas/vb+1) 
    out=[0,0]
    out[0] = fc*np.sqrt((1/qt**2-2+np.sqrt((2-1/qt**2)**2+4))/2)-f3
    out[1] = ((1-(qts/qt)**2)/(qts/qt)**2)-vas/vb
    return out
    
def sealed_find_vb_qt(vas,fs,f3,qts):
    return scipy.optimize.fsolve(sealed_find_vb_qt_func,[qts,vas], args=(vas, fs, f3, qts))
# usage
#             print(speakermodel.sealed_find_vb_qt(vas=float(vasllineedit.text())/1000,
#                                                 fs=float(fslineedit.text()),
#                                                 f3=float(f3lineedit.text()),
#                                                 qts=float(qtslabel.text())))
   
    

def calc_impedance(re, le, cms, mms, rms, sd, bl, vb=np.inf, loverA=np.inf):
    omegas = 1/math.sqrt(cms*mms)
    res = bl**2/rms
    les = bl**2*cms
    ces = mms/bl**2
    leb = bl**2/sd**2*vb/(1.18*345**2)
    cev = sd**2/bl**2*1.18*loverA
    qes = omegas*res*ces
    omega = np.logspace(1.3, 4.3, 10000)*2*np.pi
    Yab = -1j /( leb  * omega-1/(omega*cev))  # Ya = 1/ Za
    Zm = (1/res+1/(omega*les*1j)+omega*ces*1j + Yab)**(-1)
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
    ax.grid(True,which="both", ls=":")#,color="0.65")
    ax2.grid(True,which="both", ls=":")#,color="0.65")
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
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
    ax_power.set_title('Speaker Performance')
    ax_power.set_ylabel('SPL (dB 1W1m)')
    ax_phase.set_ylabel('Phase (degrees)')
    ax_groupdelay.set_ylabel('Group Delay (ms)')
    ax_groupdelay.set_xlabel('Frequency (Hz)')
    ax_power.set_xscale('log')
    ax_power.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    #ax_power.set_yscale('log')
    ax_phase.set_xscale('log')
    ax_phase.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax_groupdelay.set_xscale('log')
    ax_groupdelay.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%d"))
    ax_power.grid(True,which="both", ls=":")#,color="0.65")
    ax_phase.grid(True,which="both", ls=":")#,color="0.65")
    ax_groupdelay.grid(True,which="both", ls=":")#,color="0.65")
    fig2.show()
