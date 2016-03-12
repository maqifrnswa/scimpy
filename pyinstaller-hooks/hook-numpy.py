# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:49:51 2016

@author: http://stackoverflow.com/questions/35478526/
pyinstaller-numpy-intel-mkl-fatal-error-cannot-load-mkl-intel-thread-dll
"""

from PyInstaller import log as logging 
from PyInstaller import compat
from os import listdir

libdir = compat.base_prefix + "/Library/bin"
#mkllib = list(filter(lambda x : x.startswith('mkl_'), listdir(libdir)))
mkllib = [x for x in listdir(libdir) if x.startswith('mkl_')]
if mkllib != []:
    logger = logging.getLogger(__name__)
    logger.info("MKL installed as part of numpy, importing that!")
#    binaries = list(map(lambda l: (libdir + "/" + l, ''), mkllib))
    binaries = [(libdir + "/" + l, '') for l in mkllib]
