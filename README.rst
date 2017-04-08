.. image:: 
   https://ci.appveyor.com/api/projects/status/nbab5l0lkaqwie2u?svg=true
   :width: 100 
   :target: https://ci.appveyor.com/project/maqifrnswa/scimpy
   :alt: Appveyor build status

Scimpy
======

Scimpy is an open-source, cross-platform loudspeaker design tool. Features include:

* Modeling speaker impedance, phase, SPL, and group delay from TS Parameters

* Measuring speaker impedance using your sound card as a signal generator and
  data acquisition system

* Extract TS parameters from measured results and downloaded ZMA files.

* Loudspeaker cabinet design: the tool will calculate speaker performance (SPL
  and group delay) for sealed and vented box designs. Will calculate "optimal"
  cabinet dimensions for traditional speaker alignments (B2 closed box,
  QB4-B4-C4)

* A complete book covering speaker design theory

Scimpy is short for "Sound Card Impedance Measurements in PYthon"

Easy Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ubuntu
^^^^^^

To install:

::

    sudo add-apt-repository ppa:showard314/scimpy
    sudo apt-get update
    sudo apt-get install scimpy

To keep up to date:

::

    sudo apt-get update
    sudo apt-get upgrade

You will to reinstall after you upgrade between Ubuntu versions

Windows
^^^^^^^
Download from https://ci.appveyor.com/project/maqifrnswa/scimpy/build/artifacts

More advanced installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

PyPi Package:
^^^^^^^^^^^^^

PyPi package available (https://pypi.python.org/pypi/scimpy). To use the PyPi
scimpy package, you need to install SciPy first. SciPy is not on PyPi, so you
first must install via conda (Windows) or your package manager (Linux). Info
below, however, this is still pre-release software, so the github version will
have more features and possibly less bugs than the pypi version for now.
 

Debian/Ubuntu Development Environment & Execution:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    sudo apt-get install python3-scipy python3-pyaudio python3-matplotlib python3-pyqt5 python3-pandas
    python3 run.py


Minimal Windows Python Environment & Scimpy Installation:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Install miniconda (32bit, even if you have 64 bit - makes things easier)
from: http://conda.pydata.org/miniconda.html

Open Windows PowerShell (Start Menu, search for "Windows PowerShell")
and type the following commands:

::

    conda update conda
    conda install matplotlib scipy numpy pandas pyqt git
    pip install pyaudio
    git clone git@github.com:maqifrnswa/scimpy.git
    cd scimpy
    python run.py

To run, open PowerShell

::

    cd scimpy
    python run.py

To update to the newest version of scimpy

::

    cd scimpy
    git pull

    

Book
~~~~

LaTeX (e.g., MiKTeX)


License
~~~~~~~

Code: GPL3

Book/Documentation: CC-BY-SA 4.0


Other Open Sourced Audio Analysis Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MATAA: A Free Computer-Based Audio Analysis System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"MATAA is an extremely flexible and versatile audio analysis system. Similarly to many other computer-based audio analysis systems, MATAA applies a test signal to the device under test and simultaneously records the response signal for subsequent analysis. MATAA uses the computers built-in soundcard (or an external audio module) to play and record test signals to and from a device under test.

MATAA runs on all sorts of computer platforms because it uses Matlab or GNU Octave as a base (these are powerful number crunching programs which provide a huge toolbox of routines for data analysis and processing). This explains why MATAA is so flexible and easily extendible with custom test signals, data analyses, plotting procedures, and scrips to automate routine measurements.

MATAA is distributed as free software under the GNU General Public License."
http://audioroot.net/mataa-mats-audio-analyzer/
http://audioroot.net/wp-content/uploads/2014/08/MATAA_aX.pdf
https://github.com/mbrennwa/mataa



