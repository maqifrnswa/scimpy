# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:25:10 2016

@author: showard
"""

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi


class PlotCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

        self.axes1 = self.fig.add_subplot(221)
        self.axes2 = self.fig.add_subplot(223)
        self.axes3 = self.fig.add_subplot(322)
        self.axes4 = self.fig.add_subplot(324)
        self.axes5 = self.fig.add_subplot(326)


#        self.axes1 = fig.add_subplot(311)
#        self.axes2 = fig.add_subplot(312)
#        self.axes3 = fig.add_subplot(313)

        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes1.plot(t, s)
        self.axes2.plot(t, s)
        self.axes3.plot(t, s)
        self.axes4.plot(t, s)
        self.axes5.plot(t, s)

    def clear_axes(self):
        for axes in self.fig.axes:
            axes.cla()


