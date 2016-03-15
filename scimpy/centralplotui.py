# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:25:10 2016

@author: showard
"""

import os
import csv
import matplotlib.axes
from matplotlib.backends.backend_qt4agg import\
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi
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
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes1.plot(t, s, 'b-')
        self.axes2.plot(t, s, 'r-')
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
        self.fig.clf()
        self.init_axes()


class CentralWidget(QtGui.QWidget):
    def __init__(self):
        def saveimpedance():
            basedirectory = QtGui.QDesktopServices.storageLocation(
                QtGui.QDesktopServices.DataLocation)
            impdir = basedirectory+"/plots"
            if not os.path.isdir(impdir):
                os.makedirs(impdir)
            filters = "Impedance (*.ZRA);;All Files (*.*)"
            filename = QtGui.QFileDialog.getSaveFileName(self,
                                                         "Save Impedance Data",
                                                         impdir,
                                                         filters)
            if os.path.splitext(filename)[1] == "":
                filename = filename+".ZRA"
            print(self.canvas.axes1.get_lines()[0])
            try:
                data = zip(self.canvas.axes1.get_lines()[0].get_xdata(),
                           self.canvas.axes1.get_lines()[0].get_ydata(),
                           self.canvas.axes1b.get_lines()[0].get_ydata())
            except IndexError:
                data = zip(self.canvas.axes1.get_lines()[0].get_xdata(),
                           self.canvas.axes1.get_lines()[0].get_ydata())
            with open(filename, 'w') as outfile:
                writer = csv.writer(outfile, delimiter=' ')
                for row in data:
                    writer.writerow(row)

        super(CentralWidget, self).__init__()
        layout = QtGui.QVBoxLayout()
        toolbar = QtGui.QToolBar()

        newaction = QtGui.QAction("Save .ZRA", self)
        newaction2 = QtGui.QAction("Load .ZRA", self)
        newaction3 = QtGui.QAction("Toolbar Change with different plots", self)
        toolbar.addAction(newaction)
        toolbar.addAction(newaction2)
        toolbar.addAction(newaction3)

        newaction.triggered.connect(saveimpedance)
        self.canvas = PlotCanvas()

        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
