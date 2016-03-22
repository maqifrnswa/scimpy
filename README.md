# Scimpy
Scimpy Speaker Design Tool
Open Source Sound Card Based Speaker Impedance Measurements, Speaker Design Tool, and Book on Loudspeaker Operation

## Requirements
Python 3, Qt4, PortAudio

### General Python Requirements:

scipy, pyaudio, matplotlib, pandas and either pyqt4 or pyside

### Debian/Ubuntu development environment:

```
sudo apt-get install python3-scipy python3-pyaudio python3-matplotlib python3-pyside python3-pandas
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

PyInstaller works. First install pyinstaller:

```
pip install pywin32 pyinstaller
conda install setuptools=19.2
```

(downgrading setuptools: https://github.com/pyinstaller/pyinstaller/issues/1781)

The run

```
pyinstaller -F --additional-hooks-dir=pyinstaller-hooks run.py
```

to get a single executable in dist/



### Book
LaTeX (e.g., MiKTeX)
http://miktex.org/

## License
Code: GPL3

Book/Documentation: CC-BY-SA 4.0
