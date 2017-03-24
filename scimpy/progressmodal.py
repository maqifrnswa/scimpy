# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:55:51 2016

@author: showard
"""

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets

class ProgressModal(QtWidgets.QDialog):
    super(ProgressModal, self).__init__()
    self.progressbar = QtWidgets.QProgressDialog
