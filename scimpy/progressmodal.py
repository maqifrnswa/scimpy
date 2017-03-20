# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:55:51 2016

@author: showard
"""

from matplotlib.backends import qt_compat
from matplotlib import use
use('Qt4Agg')
USE_PYSIDE = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if USE_PYSIDE:
    from PySide import QtGui
else:
    from PyQt4 import QtGui

class ProgressModal(QtGui.QDialog):
    super(ProgressModal, self).__init__()
    self.progressbar = QtGui.QProgressDialog
