from setuptools import setup, find_packages
try:
    import py2exe
except:
    pass


setup(
    name = "scimpy",
    version = "0.0.dev0",
    description ="Scimpy Speaker Design Tool",
    url = "https://github.com/maqifrnswa/scimpy",
    author = "Scott Howard",
    license = "GPLv3+",
    classifiers = [
        "Development Status :: 3 - Alpha",
	"Environment :: MacOS X",
	"Environment :: X11 Applications :: Qt",
	"Environment :: Win32 (MS Windows)",
	"Environment :: X11 Applications",
	"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
	"Natural Language :: English",
	"Operating System :: MacOS",
	"Operating System :: Microsoft :: Windows",
	"Programming Language :: Python :: 3",
	"Topic :: Artistic Software",
	"Topic :: Multimedia :: Sound/Audio",
	"Topic :: Scientific/Engineering :: Physics"],
    install_requries=["scipy", "numpy", "matplotlib", "pyaudio", "pandas"],
    packages = find_packages(),
    entry_points = {
        'gui_scripts': [
            'scimpy = scimpy.scimpyui:main'
        ]
    },
    windows = ['run.py']  # py2exe support
)
