# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:49:51 2016

@author: http://stackoverflow.com/questions/35478526/
pyinstaller-numpy-intel-mkl-fatal-error-cannot-load-mkl-intel-thread-dll
"""

from PyInstaller import log as logging 
from PyInstaller import compat
from os import listdir

try:
    libdir = compat.base_prefix + "/Library/bin"
    mkllib = [x for x in listdir(libdir) if x.startswith('mkl_')]
    if mkllib != []:
        logger = logging.getLogger(__name__)
        logger.info("MKL installed as part of numpy, importing that!")
        binaries = [(libdir + "/" + l, '') for l in mkllib]
except FileNotFoundError:
    pass
