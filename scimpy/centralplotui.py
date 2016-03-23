# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:25:10 2016

@author: showard
"""
import scimpy.speakermodel as speakermodel
import os
import csv
import pandas
import matplotlib.axes
from matplotlib.backends.backend_qt4agg import\
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends import qt_compat
USE_PYSIDE = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if USE_PYSIDE:
    from PySide import QtGui
else:
    from PyQt4 import QtGui


class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self):
        self.fig = Figure()
        super(PlotCanvas, self).__init__(self.fig)
        self.axes1 = None
        self.axes1b = None
        self.axes2 = None
        self.axes2b = None
        self.init_axes()
        self.placeholder()

    def placeholder(self):
        t__ = np.arange(0.0, 3.0, 0.01)
        s__ = np.sin(2*np.pi*t__)
        self.axes1.plot(t__, s__, 'b-')
        self.axes2.plot(t__, s__, 'r-')
        self.axes1.grid(True, which="both", color="0.65", ls='-')
        self.axes2.grid(True, which="both", color="0.65", ls='-')
        self.axes1.set_xscale('log')
        self.axes1.set_xlim(right=3)
        self.axes2.set_title("Scimpy Speaker Designer!")

    def init_axes(self):
        self.axes1 = self.fig.add_subplot(211)
        self.axes2 = self.fig.add_subplot(212)
        self.axes1b = matplotlib.axes.Axes.twinx(self.axes1)
        self.axes2b = matplotlib.axes.Axes.twinx(self.axes2)

    def clear_axes(self):
        if self.parentWidget().holdplotaction.isChecked() == False:
            self.fig.clf()
            self.init_axes()


class CentralWidget(QtGui.QWidget):
    def __init__(self):
        def getimpdir():
            basedirectory = QtGui.QDesktopServices.storageLocation(
                QtGui.QDesktopServices.DataLocation)
            impdir = basedirectory+"/plots"
            if not os.path.isdir(impdir):
                os.makedirs(impdir)
            filters = "Impedance (*.ZDA *.ZMA);;All Files (*.*)"
            return impdir, filters

        def saveimpedance():
            impdir, filters = getimpdir()
            filename = QtGui.QFileDialog.getSaveFileName(self,
                                                         "Save Impedance Data",
                                                         impdir,
                                                         filters)
            if filename == "":
                return
            elif os.path.splitext(filename)[1] == "":
                filename = filename+".ZMA"
            print(self.canvas.axes1.get_lines()[0])
            try:
                data = zip(self.canvas.axes1.get_lines()[0].get_xdata(),
                           self.canvas.axes1.get_lines()[0].get_ydata(),
                           self.canvas.axes1b.get_lines()[0].get_ydata())
            except IndexError:
                data = zip(self.canvas.axes1.get_lines()[0].get_xdata(),
                           self.canvas.axes1.get_lines()[0].get_ydata(),
                           [0]*len(
                               self.canvas.axes1.get_lines()[0].get_xdata()))
            with open(filename, 'w') as outfile:
                writer = csv.writer(outfile, delimiter=' ')
                for row in data:
                    writer.writerow(row)

        def loadimpedance():
            impdir, filters = getimpdir()
            filename = QtGui.QFileDialog.getOpenFileName(self,
                                                         "Load Impedance Data",
                                                         impdir,
                                                         filters)
            if filename == "":
                return

            file_data = pandas.read_csv(filename,
                                        header=None,
                                        delim_whitespace=True)

            self.canvas.clear_axes()
            speakermodel.plot_impedance(ax1=self.canvas.axes1,
                                        ax2=self.canvas.axes1b,
                                        freqs=file_data[0],
                                        magnitude=file_data[1],
                                        phase=file_data[2])
            self.canvas.draw()

        super(CentralWidget, self).__init__()
        self.canvas = PlotCanvas()
        layout = QtGui.QVBoxLayout()
        toolbar = QtGui.QToolBar()

        savezraaction = QtGui.QAction("Save .ZMA/ZDA", self)
        loadzraaction = QtGui.QAction("Load .ZMA/ZDA", self)
        self.holdplotaction = QtGui.QAction("Hold Plot Data", self)
        self.holdplotaction.setCheckable(True)
        toolbar.addAction(savezraaction)
        toolbar.addAction(loadzraaction)
        toolbar.addAction(self.holdplotaction)

        savezraaction.triggered.connect(saveimpedance)
        loadzraaction.triggered.connect(loadimpedance)

        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
