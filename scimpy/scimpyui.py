# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
try:
    from PyQt4 import QtGui, QtCore
except ImportError:
    from PySide import QtGui, QtCore
import scimpy.imptesterui as imptesterui
import scimpy.speakermodelui as speakermodelui


class SpeakerModelMainWindow(QtGui.QMainWindow):
    """Main application widget"""
    def __init__(self, title):
        super(SpeakerModelMainWindow, self).__init__()
        placeholder = QtGui.QLabel("This is where plots will go. \
            The above two tabs are floatable docks. \
            Probably arrange them verticaly on the left.")
        self.setCentralWidget(placeholder)
        self.setWindowTitle(title)

        self.imptestdock = QtGui.QDockWidget("Impedance Measurement")
        self.imptest = imptesterui.ImpTester(parent=self.imptestdock)
        self.imptestdock.setWidget(self.imptest)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.imptestdock)
        self.imptestdock.setFeatures(QtGui.QDockWidget.DockWidgetMovable |
                                     QtGui.QDockWidget.DockWidgetFloatable)

        self.speakermodeldock = QtGui.QDockWidget("Speaker Modeling")
        self.speakermodel = speakermodelui.SpeakerModelWidget()
        self.speakermodeldock.setWidget(self.speakermodel)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.speakermodeldock)
        self.tabifyDockWidget(self.speakermodeldock, self.imptestdock)
        self.speakermodeldock.setFeatures(QtGui.QDockWidget.DockWidgetMovable |
                                          QtGui.QDockWidget.
                                          DockWidgetFloatable)


def main():
    """Starts Scimpy Speaker Design Suite"""
    app = QtGui.QApplication(sys.argv)
    # imptesterwidg = imptesterui.ImpTester()
    # speakermodelwidg = speakermodelui.SpeakerModelWidget()
    # imptesterwidg.show()
    # speakermodelwidg.show()
    mainwindow = SpeakerModelMainWindow("Scimpy Speaker Designer")
    mainwindow.show()
    sys.exit(app.exec_())

