# Scimpy
Scimpy Speaker Design Tool
Open Source Sound Card Based Speaker Impedance Measurements, Speaker Design Tool, and Book on Loudspeaker Operation

## Requirements
Python 3, Qt4, PortAudio

### General Python Requirements:

scipy, pyaudio, matplotlib, and either pyqt4 or pyside

### Debian/Ubuntu development environment:

```
sudo apt-get install python3-scipy python3-pyaudio python3-matplotlib python3-pyside
```

### Windows Python Environment 
& Scimpy Installation:

#### Full install (LARGE), comes with spyder IDE and many other python packages

install anaconda (https://www.continuum.io/downloads), open anaconda console and then in the anaconda console run "pip install pyaudio".

If you want more control over the sound card, you can use a version of pyaudio built with more APIs available. Download pyaudio from:
http://www.lfd.uci.edu/~gohlke/pythonlibs/ then open the anaconda console and install pyaudio
with "pip install PyAudio-0.2.9-cp35-none-win_amd64.whl"
replacing PyAudio-0.2.9-cp35-none-win_amd64.whl with the name of the file you downloaded.

#### Minimal install:

Install miniconda (32bit, even if you have 64 bit - makes things easier) from:
http://conda.pydata.org/miniconda.html

Open Windows PowerShell (Start Menu, search for "Windows PowerShell") and type the following commands:

```
conda update conda
conda install matplotlib scipy numpy
pip install pyaudio
cd LOCATION_WHERE_SCIMPY_WAS_DOWNLOADED
python run.py
```

have fun!

#### How to build Windows binaries

Work in progress: trying to get both py2exe and pyinstaller to work

Install either with pip. py2exe hangs on finding DLLs, pyinstaller can't find pywintypes
possibly solution?
http://stackoverflow.com/questions/19280894/py2exe-no-system-module-pywintypes



### Book
LaTeX (e.g., MiKTeX)
http://miktex.org/

## License
Code: GPL3

Book/Documentation: CC-BY-SA 4.0
