# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:20:04 2016

@author: showard
"""

import sys
import argparse
import logging
import scimpy.imptesterui as imptesterui
import scimpy.speakermodelui as speakermodelui
import scimpy.centralplotui as centralplotui
import scimpy.impfitterui as impfitterui
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QDesktopServices, QUrl
import matplotlib
matplotlib.use('Qt5Agg')


class SpeakerModelMainWindow(QtWidgets.QMainWindow):
    """Main application widget"""
    def __init__(self, title):
        super(SpeakerModelMainWindow, self).__init__()
        # self.plotwidget = centralplotui.PlotCanvas()
        self.plotwidget = centralplotui.CentralWidget()
        self.setCentralWidget(self.plotwidget)
        self.setWindowTitle(title)
        self.setDockOptions(self.dockOptions() | self.VerticalTabs)

        self.statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusbar)
        # self.setCorner(QtCore.Qt.TopLeftCorner,
        #                QtCore.Qt.LeftDockWidgetArea);

        self.imptestdock = QtWidgets.QDockWidget("Impedance Measurement")
        self.imptest = imptesterui.ImpTester(self)
        self.imptestdock.setWidget(self.imptest)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.imptestdock)
        self.imptestdock.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable |
                                     QtWidgets.QDockWidget.DockWidgetFloatable)

        self.speakermodeldock = QtWidgets.QDockWidget("Speaker Modeling")
        self.speakermodel = speakermodelui.SpeakerModelWidget()
        # until speaker edit tool is written, put in scroll area
        tempscrollarea = QtWidgets.QScrollArea()
        tempscrollarea.setWidget(self.speakermodel)
        tempscrollarea.setAlignment(QtCore.Qt.AlignCenter)
        # self.speakermodeldock.setWidget(self.speakermodel)
        self.speakermodeldock.setWidget(tempscrollarea)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.speakermodeldock)
        self.tabifyDockWidget(self.speakermodeldock, self.imptestdock)
        self.speakermodeldock.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable |
                                          QtWidgets.QDockWidget.
                                          DockWidgetFloatable)
        self.impfitterdock = QtWidgets.QDockWidget("Impedance Fitter")
        self.impfitterwidget = impfitterui.ImpedanceFitterWidget()
        self.impfitterdock.setWidget(self.impfitterwidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.impfitterdock)
        self.impfitterdock.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable |
                                       QtWidgets.QDockWidget.DockWidgetFloatable)
        self.tabifyDockWidget(self.imptestdock, self.impfitterdock)
        
        self.speakermodeldock.raise_()

        self.init_menus()
#        self.init_toolbar()

    def helptriggeraction(self):
        QDesktopServices.openUrl(QUrl(
                "https://maqifrnswa.github.io/scimpy/doc/html/scimpy.html"))

    def init_menus(self):
        filemenu = self.menuBar().addMenu("&File")
        newaction = QtWidgets.QAction("&New", self)
        filemenu.addAction(newaction)

        helpmenu = self.menuBar().addMenu("&Help")
        helpaction = QtWidgets.QAction("&Help", self)
        helpaction.triggered.connect(self.helptriggeraction)
        helpmenu.addAction(helpaction)

#    def init_toolbar(self):
#        filetoolbar = self.addToolBar("test")
#        newaction = QtWidgets.QAction("Testing", self)
#        newaction = QtWidgets.QAction("Testing", self)
#        newaction2 = QtWidgets.QAction("Testing2", self)
#        filetoolbar.addAction(newaction)
#        filetoolbar.addAction(newaction2)

    def center(self):
        """Method to center widget on screen"""
        framegeo = self.frameGeometry()
        centerpoint = QtWidgets.QApplication.desktop().availableGeometry().center()
        framegeo.moveCenter(centerpoint)
        self.move(framegeo.topLeft())


def parse_arguments():
    parser = argparse.ArgumentParser(description='Scimpy Speaker Design Suite')
    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help="Increase logging level (-v info, -vv debug)")
    args = parser.parse_args()
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels)-1,args.verbose)]
    logging.basicConfig(level=level)


def main():
    """Starts Scimpy Speaker Design Suite"""
    parse_arguments()
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("scimpy")
    # imptesterwidg = imptesterui.ImpTester()
    # speakermodelwidg = speakermodelui.SpeakerModelWidget()
    # imptesterwidg.show()
    # speakermodelwidg.show()
    mainwindow = SpeakerModelMainWindow("Scimpy Speaker Designer")
    mainwindow.show()
    mainwindow.center()
    sys.exit(app.exec_())
