# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:03 2016

@author: showard
"""

import numpy as np
import scipy.optimize
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui
else:
    from PyQt4 import QtGui


# TODO put all the find_main_window functions in one module, just call that
def find_main_window():
    for widget in QtGui.QApplication.topLevelWidgets():
        if isinstance(widget, QtGui.QMainWindow):
            return widget


def free_speaker_extract():
    def residuals(x0, omega, zmag, zphase):
        re_, le_, res, ces, les = x0
        zelect = (1/res+1/(omega*les*1j)+omega*ces*1j)**(-1)
        ztotal = zelect+re_+omega*le_*1j
        diff = ztotal - zmag * np.exp(1j*zphase)
        z1d = np.zeros(diff.size*2, dtype=np.float64)
        z1d[0:z1d.size:2] = diff.real
        z1d[1:z1d.size:2] = diff.imag
        #print(ztotal[100], zmag[100] * np.exp(1j*zphase[100]))
        return sum(z1d**2)

    plotwidget = find_main_window().plotwidget.canvas
    try:
        omega = plotwidget.axes1.get_lines()[0].get_xdata()*2.0*np.pi
        zmag = plotwidget.axes1.get_lines()[0].get_ydata()
        zphase = plotwidget.axes1b.get_lines()[0].get_ydata()/180.0*np.pi
    except IndexError:
        print("need to impliment if file only has zeros for phase")
    def print_fun(x, f, accepted):
        if int(accepted)==1:
            print("at minima %.4f accepted %d" % (f, int(accepted)),x)


    class StepFunc():
        def __init__(self, stepsize=.9):
            self.stepsize = stepsize

        def __call__(self, x):
            s = self.stepsize
            xout = [max([0, np.random.uniform(k*(1-s), k*(1+s))])
                    for k in x]
            # print(xout)
            return xout

    stepfuncobj = StepFunc()
# TODO basinhop only positive numbers!
    print( scipy.optimize.basinhopping(residuals,
                                    #x0=(6, 1e-4, 4.5**2/3.4, 1.8e-3/4.5**2, .16e-3*4.5**2),
                                    x0=[10,.1,10,.1,.1],#x0=[6, 1e-4, 6, 1e-4, 1e-4],
callback=print_fun,
niter=2000,
                                    minimizer_kwargs={"args":( omega, zmag, zphase)},
take_step=stepfuncobj))


class ImpedanceFitterWidget(QtGui.QGroupBox):
    """Widget for modeling speaker performance based on T/S values"""
    def __init__(self):
        super(ImpedanceFitterWidget, self).__init__("Equiv. Electrical Model")
        self.driver_params = {}
        self.init_ui()

    def init_ui(self):
        """Method to initialize UI and widget callbacks"""
        #formwidget = QtGui.QGroupBox("Equiv. Electrical Model")
        formwidgetlayout = QtGui.QFormLayout()

        relineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Re (ohms):", relineedit)
        lelineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Le (mH):", lelineedit)
        reslineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Res (ohms):", reslineedit)
        leslineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Les (mH):", leslineedit)
        ceslineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Ces (mH):", ceslineedit)
        formwidgetlayout.addRow("Rel (ohms):", reslineedit)
        leslineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Leb (mH):", leslineedit)
        ceslineedit = QtGui.QLineEdit()
        formwidgetlayout.addRow("Cev (mH):", ceslineedit)

        freespeakerbtn = QtGui.QPushButton("Extract Free Speaker Params")
        freespeakerbtn.clicked.connect(free_speaker_extract)
        formwidgetlayout.addRow(freespeakerbtn)
        closedboxbtn = QtGui.QPushButton("Calculate Closed Box Params")
        formwidgetlayout.addRow(closedboxbtn)

        portedboxbtn = QtGui.QPushButton("Calculate Ported Box Params")
        formwidgetlayout.addRow(portedboxbtn)


#        layout = QtGui.QGridLayout()
#        layout.addWidget(formwidget, 0, 0, 1, 3)
#        layout.addWidget(freespeakerbtn, 1, 0, 1, 1)
#        layout.addWidget(closedboxbtn, 1, 1, 1, 1)
#        layout.addWidget(portedboxbtn, 1, 2, 1, 1)

        self.setLayout(formwidgetlayout)
