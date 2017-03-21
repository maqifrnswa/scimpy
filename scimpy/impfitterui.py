# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:03 2016

@author: showard
"""

import numpy as np
import scipy.optimize
from matplotlib import use
use('Qt4Agg')
from matplotlib.backends import qt_compat
USE_PYSIDE = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if USE_PYSIDE:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore


# TODO put all the find_main_window functions in one module, just call that
def find_main_window():
    for widget in QtGui.QApplication.topLevelWidgets():
        if isinstance(widget, QtGui.QMainWindow):
            return widget


# TODO Don't use a function, use this worker instead
# needs to be updated with new fit function below
#class FreeSpeakerExtract(QtCore.QThread):
#    updateProgress = QtCore.Signal(int)
#
#    def __init__(self, init_test):
#        super(FreeSpeakerExtract, self).__init__()
#        self.init_test = init_test
#        self.result = []
#
#    def run(self):
#        class Residuals():
#            def __init__(self, omega, zmag, zphase):
#                self.omega = omega
#                self.zmag = zmag
#                self.zphase = zphase
#
#            def __call__(self, x0):
#                # TODO weight each residual by the derivative (diff) of log(omega)
#                # this way when data is linear (FFT) we don't over-emphasize
#                # high omega points
#                omega = self.omega
#                zmag = self.zmag
#                zphase = self.zphase
#                re_, le_, res, ces, les, reddy = x0
#                zelect = (1/res+1/(omega*les*1j)+omega*ces*1j)**(-1)
#                # ztotal = zelect+re_+omega*le_*1j
#                ztotal = zelect+re_+(1/omega*le_*1j+1/reddy)**(-1)
#                diff = ztotal - zmag * np.exp(1j*zphase)
#                z1d = np.zeros(diff.size*2, dtype=np.float64)
#                z1d[0:z1d.size:2] = diff.real
#                z1d[1:z1d.size:2] = diff.imag
#                # print(ztotal[100], zmag[100] * np.exp(1j*zphase[100]))
#                # sse = sum(z1d**2)
#                # if sse > sse.size:
#                #    return sum(z1d**2)
#                return sum(z1d**2)
#                # return sum((abs(ztotal)-zmag)**2)
#
#        def print_fun(x, f, accepted):
#            if int(accepted) == 1:
#                print("at minima %.4f accepted %d" % (f, int(accepted)), x)
#
#        class StepFunc():
#            def __init__(self, stepsize, init_test):
#                self.stepsize = stepsize
#                self.init_test = init_test
#
#            def __call__(self, x):
#                s = self.stepsize
#                # xout = x+ self.init_test * np.random.uniform(-s, s, len(x))
#                # xout = x + x * np.random.uniform(-s, s, len(x))
#                # xout = x+self.init_test*np.random.normal(0, s, len(x))
#                xout = x+x*np.random.normal(0, s, len(x))
#                # xout = x+[np.random.normal(0, s*element) for element in self.init_test]
#                return xout
#
#        def accept_test_func(f_new, x_new, f_old, x_old):
#            if (x_new[0] > 1 and
#                    x_new[2] > 1 and
#                    all(element > 0 for element in x_new)):
#                return True
#            return False
#
#        plotwidget = find_main_window().plotwidget.canvas
#        try:
#            omega = plotwidget.axes1.get_lines()[0].get_xdata()*2.0*np.pi
#            zmag = plotwidget.axes1.get_lines()[0].get_ydata()
#            zphase = plotwidget.axes1b.get_lines()[0].get_ydata()/180.0*np.pi
#        except IndexError:
#            print("need to impliment if file only has zeros for phase")
#
#        #init_test = [10, .01, 10, .01, .01]  # TODO: Ask use for starting point?
#        stepsize = .5
#        stepfuncobj = StepFunc(stepsize=stepsize, init_test=self.init_test)
#        residuals_obj = Residuals(omega, zmag, zphase)
#        output = scipy.optimize.basinhopping(residuals_obj,
#                                             x0=self.init_test,
#                                             callback=print_fun,
#                                             niter=200,
#                                             accept_test=accept_test_func,
#                                             take_step=stepfuncobj)
#        print(output.keys())
#        output = output["x"]
#        print([output, "re: ", output[0], "le: ", output[1], "rms: ",
#               4.5**2/output[2], "mms: ", output[3]*4.5**2, "cms: ",
#               output[4]/4.5**2])
#        self.result = output


def free_speaker_extract(init_test, progressdialog):
    class Residuals():
        def __init__(self, omega, zmag, zphase):
            self.omega = omega
            self.zmag = zmag
            self.zphase = zphase
            self.weights = np.gradient(np.log10(omega))

        def __call__(self, x0):
            # Possibly give option to restrict fit range?
            # TODO: first fit to 1k Hz, no reddy - then do reddy next
            omega = self.omega
            zmag = self.zmag
            zphase = self.zphase
            weights = self.weights
            # re_, le_, res, ces, les, reddy = x0 w/ reddy
            re_, le_, res, ces, les, reddy = x0
            zelect = (1/res+1/(omega*les*1j)+omega*ces*1j)**(-1)
            # ztotal = zelect+re_+omega*le_*1j
            ztotal = zelect+re_+(1/(omega*le_*1j)+1/reddy)**(-1)
            diff = ztotal - zmag * np.exp(1j*zphase)
            z1d = np.zeros(diff.size*2, dtype=np.float64)
            # since omega is linear, and we are interested in log(omega)
            # weight each by the gradient of log omega
            z1d[0:z1d.size:2] = diff.real * weights # just weight one since they will multiply
            z1d[1:z1d.size:2] = diff.imag * weights
            # print(ztotal[100], zmag[100] * np.exp(1j*zphase[100]))
            # sse = sum(z1d**2)
            # if sse > sse.size:
            #    return sum(z1d**2)
            return sum(z1d**2) # old, unweighted
            # return sum((abs(ztotal)-zmag)**2)

    def print_fun(x, f, accepted):
        if int(accepted) == 1:
            print("at minima %.4f accepted %d" % (f, int(accepted)), x)

    class StepFunc():
        def __init__(self, stepsize, init_test):
            self.stepsize = stepsize
            self.init_test = init_test

        def __call__(self, x):
            s = self.stepsize
            # xout = x+ self.init_test * np.random.uniform(-s, s, len(x))
            # xout = x + x * np.random.uniform(-s, s, len(x))
            # xout = x+self.init_test*np.random.normal(0, s, len(x))
            # xout = x+x*np.random.normal(0, s, len(x))
            xout = x + [np.random.normal(0, s*element) for element in self.init_test]
            xout = [max([0.001, element]) for element in xout]
            return xout

    def accept_test_func(f_new, x_new, f_old, x_old):
        # might not be needed...
        return bool(np.all(x_new > 0))

    plotwidget = find_main_window().plotwidget.canvas
    try:
        omega = plotwidget.axes1.get_lines()[0].get_xdata()*2.0*np.pi
        zmag = plotwidget.axes1.get_lines()[0].get_ydata()
        zphase = plotwidget.axes1b.get_lines()[0].get_ydata()/180.0*np.pi
    except IndexError:
        print("need to impliment if file only has zeros for phase")

    # init_test = [10, .01, 10, .01, .01]  # TODO: Ask use for starting point?
    stepsize = .5
    stepfuncobj = StepFunc(stepsize=stepsize, init_test=init_test)
    residuals_obj = Residuals(omega, zmag, zphase)
    output = scipy.optimize.basinhopping(residuals_obj,
                                         x0=init_test,
                                         callback=print_fun,
                                         niter_success=200,
                                         # accept_test=accept_test_func,
                                         take_step=stepfuncobj)
    print(output.keys())
    output = output["x"]
    print([output, "re: ", output[0], "le: ", output[1], "rms: ",
           4.5**2/output[2], "mms: ", output[3]*4.5**2, "cms: ",
           output[4]/4.5**2])
    return output


class ImpedanceFitterWidget(QtGui.QGroupBox):
    """Widget for modeling speaker performance based on T/S values"""
    def __init__(self):
        super(ImpedanceFitterWidget, self).__init__("Equiv. Electrical Model")
        self.init_ui()

    def init_ui(self):
        """Method to initialize UI and widget callbacks"""
        def freespeakerbtn_handler():
            progressdialog = QtGui.QProgressDialog("Finding Fit Values",
                                                   "Cancel",
                                                   0,
                                                   100)
            blproduct = float(bllineedit.text())
            init_test = [float(relineedit.text()),
                         float(lelineedit.text())/1000,
                         blproduct**2/float(rmslineedit.text()),
                         float(mmslineedit.text())/blproduct**2/1000,
                         float(cmslineedit.text())*blproduct**2/1000,
                         float(reddylineedit.text())]
            fitresult = free_speaker_extract(init_test, progressdialog)
            # worker = FreeSpeakerExtract(init_test)
            # progressdialog.exec()
            # get fitresult from worker
            relineedit.setText("{0:.2g}".format(fitresult[0]))
            lelineedit.setText("{0:.2g}".format(fitresult[1]*1000))
            rmslineedit.setText("{0:.2g}".format(blproduct**2/fitresult[2]))
            mmslineedit.setText("{0:.2g}".format(fitresult[3]*blproduct**2*1000))
            cmslineedit.setText("{0:.2g}".format(fitresult[4]/blproduct**2*1000))
            reddylineedit.setText("{0:.2g}".format(fitresult[5]))
            progressdialog.setValue(100)

        def export_to_model_btn_handler():
            speakermodel = find_main_window().speakermodel
            speakermodel.relineedit.setText(str(relineedit.text()))
            speakermodel.lelineedit.setText(str(lelineedit.text()))
            speakermodel.cmslineedit.setText(str(cmslineedit.text()))
            speakermodel.mmslineedit.setText(str(mmslineedit.text()))
            speakermodel.rmslineedit.setText(str(rmslineedit.text()))
            speakermodel.bllineedit.setText(str(bllineedit.text()))


        formwidgetlayout = QtGui.QFormLayout()

        bllineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("*BL (Tm):", bllineedit)
        relineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("Re (ohms):", relineedit)
        lelineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("Le (mH):", lelineedit)
        rmslineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("Rms (ohms):", rmslineedit)
        mmslineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("Mms (g):", mmslineedit)
        cmslineedit = QtGui.QLineEdit("1")
        formwidgetlayout.addRow("Cms (mm/N):", cmslineedit)
        reddylineedit = QtGui.QLineEdit("100000")
        formwidgetlayout.addRow("Reddy (ohms):", reddylineedit)
#        formwidgetlayout.addRow("Leb (mH):", leslineedit)
#        ceslineedit = QtGui.QLineEdit()
#        formwidgetlayout.addRow("Cev (mH):", ceslineedit)

        freespeakerbtn = QtGui.QPushButton("Extract Free Speaker Params")
        freespeakerbtn.clicked.connect(freespeakerbtn_handler)
        formwidgetlayout.addRow(freespeakerbtn)
        export_to_model_btn = QtGui.QPushButton("Export to Speaker Modeler")
        formwidgetlayout.addRow(export_to_model_btn)
        export_to_model_btn.clicked.connect(export_to_model_btn_handler)

        self.setLayout(formwidgetlayout)
