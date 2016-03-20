# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
import scimpy.imptesterui as imptesterui
import scimpy.speakermodelui as speakermodelui
import scimpy.centralplotui as centralplotui
import scimpy.impfitterui as impfitterui

from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
    from PySide import QtGui, QtCore
else:
    from PyQt4 import QtGui, QtCore


class SpeakerModelMainWindow(QtGui.QMainWindow):
    """Main application widget"""
    def __init__(self, title):
        super(SpeakerModelMainWindow, self).__init__()
        # self.plotwidget = centralplotui.PlotCanvas()
        self.plotwidget = centralplotui.CentralWidget()
        self.setCentralWidget(self.plotwidget)
        self.setWindowTitle(title)
        self.setDockOptions(self.dockOptions() | self.VerticalTabs)

        self.statusbar = QtGui.QStatusBar()
        self.setStatusBar(self.statusbar)
        # self.setCorner(QtCore.Qt.TopLeftCorner,
        #                QtCore.Qt.LeftDockWidgetArea);

        self.imptestdock = QtGui.QDockWidget("Impedance Measurement")
        self.imptest = imptesterui.ImpTester(self)
        self.imptestdock.setWidget(self.imptest)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.imptestdock)
        self.imptestdock.setFeatures(QtGui.QDockWidget.DockWidgetMovable |
                                     QtGui.QDockWidget.DockWidgetFloatable)

        self.speakermodeldock = QtGui.QDockWidget("Speaker Modeling")
        self.speakermodel = speakermodelui.SpeakerModelWidget()
        # until speaker edit tool is written, put in scroll area
        tempscrollarea = QtGui.QScrollArea()
        tempscrollarea.setWidget(self.speakermodel)
        tempscrollarea.setAlignment(QtCore.Qt.AlignCenter)
        # self.speakermodeldock.setWidget(self.speakermodel)
        self.speakermodeldock.setWidget(tempscrollarea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.speakermodeldock)
        self.tabifyDockWidget(self.speakermodeldock, self.imptestdock)
        self.speakermodeldock.setFeatures(QtGui.QDockWidget.DockWidgetMovable |
                                          QtGui.QDockWidget.
                                          DockWidgetFloatable)
        self.impfitterdock = QtGui.QDockWidget("Impedance Fitter")
        self.impfitterwidget = impfitterui.ImpedanceFitterWidget()
        self.impfitterdock.setWidget(self.impfitterwidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.impfitterdock)
        self.impfitterdock.setFeatures(QtGui.QDockWidget.DockWidgetMovable |
                                     QtGui.QDockWidget.DockWidgetFloatable)
        self.tabifyDockWidget(self.imptestdock, self.impfitterdock)

        self.init_menus()
        self.init_toolbar()

    def init_menus(self):
        filemenu = self.menuBar().addMenu("&File")
        newaction = QtGui.QAction("&New", self)
        filemenu.addAction(newaction)

    def init_toolbar(self):
        filetoolbar = self.addToolBar("test")
        newaction = QtGui.QAction("Testing", self)
        newaction = QtGui.QAction("Testing", self)
        newaction2 = QtGui.QAction("Testing2", self)
        filetoolbar.addAction(newaction)
        filetoolbar.addAction(newaction2)

    def center(self):
        """Method to center widget on screen"""
        framegeo = self.frameGeometry()
        centerpoint = QtGui.QApplication.desktop().availableGeometry().center()
        framegeo.moveCenter(centerpoint)
        self.move(framegeo.topLeft())


def main():
    """Starts Scimpy Speaker Design Suite"""
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("scimpy")
    # imptesterwidg = imptesterui.ImpTester()
    # speakermodelwidg = speakermodelui.SpeakerModelWidget()
    # imptesterwidg.show()
    # speakermodelwidg.show()
    mainwindow = SpeakerModelMainWindow("Scimpy Speaker Designer")
    mainwindow.show()
    mainwindow.center()
    sys.exit(app.exec_())
