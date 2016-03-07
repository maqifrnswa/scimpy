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

### Windows Python environment set-up:

install anaconda (https://www.continuum.io/downloads), open anaconda console and then in the anaconda console run "pip install pyaudio".

If you want more control over the sound card, you can use a version of pyaudio built with more APIs available. Download pyaudio from:
http://www.lfd.uci.edu/~gohlke/pythonlibs/ then open the anaconda console and install pyaudio
with "pip install PyAudio-0.2.9-cp35-none-win_amd64.whl"
replacing PyAudio-0.2.9-cp35-none-win_amd64.whl with the name of the file you downloaded.


### Book
LaTeX (e.g., MiKTeX)
http://miktex.org/

## License
Code: GPL3

Book/Documentation: CC-BY-SA 4.0
