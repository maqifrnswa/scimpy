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
        self.axes1 = None
        self.axes2 = None
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

    def clear_axes(self):
        self.fig.clf()
        self.init_axes()
