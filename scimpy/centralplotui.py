# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:25:10 2016

@author: showard
"""
import os
import csv
import pandas
import matplotlib.axes
import numpy as np
from PyQt5 import QtWidgets, QtCore
import scimpy.speakermodel as speakermodel
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self):
        self.fig = Figure(tight_layout=True)
        super(PlotCanvas, self).__init__(self.fig)
        self.axes1 = None
        self.axes1b = None
        self.axes2 = None
        self.axes2b = None
        self.init_axes()
        self.placeholder()

    def placeholder(self):
        """Plots placeholder figure upon load"""
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
        """Adds subplots to the axes"""
        self.axes1 = self.fig.add_subplot(211)
        self.axes2 = self.fig.add_subplot(212)
        self.axes1b = matplotlib.axes.Axes.twinx(self.axes1)
        self.axes2b = matplotlib.axes.Axes.twinx(self.axes2)

    def clear_axes(self):
        """Clears the axes"""
        if self.parentWidget().holdplotaction.isChecked() is False:
            self.fig.clf()
            self.init_axes()


class CentralWidget(QtWidgets.QWidget):
    """Central widget that holds the plots"""
    def __init__(self):
        def getimpdir():
            """

            :returns: directory plots are stored and the filters to use for
            Qt's file dialogs

            :rtype: str, str

            """
            # Used to stopre in AppDataLocation, but was kind of hidden...
            basedirectory = QtCore.QStandardPaths.writableLocation(
                QtCore.QStandardPaths.DocumentsLocation)
            impdir = basedirectory+"/Scimpy/plots"
            if not os.path.isdir(impdir):
                os.makedirs(impdir)
            filters = "Impedance Files (*.ZDA *.ZMA);;All Files (*.*)"
            return impdir, filters

        def saveimpedance():
            """Saves active plots held on the widget"""
            impdir, filters = getimpdir()
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "Save Impedance Data", impdir, filters)
            if filename == "":
                return
            elif os.path.splitext(filename)[-1] == "":
                filename = filename+".ZMA"
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
            """Loads previously saved plots on to the widget"""
            impdir, filters = getimpdir()
            filename = QtWidgets.QFileDialog.getOpenFileName(
                self, "Load Impedance Data", impdir, filters)
            if filename == "":
                return

            file_data = pandas.read_csv(str(filename),
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
        layout = QtWidgets.QVBoxLayout()
        toolbar = QtWidgets.QToolBar()

        savezraaction = QtWidgets.QAction("Save .ZMA/ZDA", self)
        loadzraaction = QtWidgets.QAction("Load .ZMA/ZDA", self)
        self.holdplotaction = QtWidgets.QAction("Hold Plot Data", self)
        self.holdplotaction.setCheckable(True)
        toolbar.addAction(savezraaction)
        toolbar.addAction(loadzraaction)
        toolbar.addAction(self.holdplotaction)

        savezraaction.triggered.connect(saveimpedance)
        loadzraaction.triggered.connect(loadimpedance)

        mpl_toolbar = NavigationToolbar(self.canvas, self.parentWidget())

#        toolbarwidget=QtWidgets.QWidget()
#        layout2=QtWidgets.QHBoxLayout()
#        layout2.addWidget(toolbar)
#        layout2.addWidget(mpl_toolbar)
#        toolbarwidget.setLayout(layout2)
#        layout.addWidget(toolbarwidget)

        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(mpl_toolbar)
        self.setLayout(layout)
