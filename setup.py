from setuptools import setup, find_packages
try:
    import py2exe
except:
    pass

setup(
    name = "scimpy",
    version = "0.0.dev1",
    packages = find_packages(),
    entry_points = {
        'gui_scripts': [
            'scimpy = scimpy.scimpyui:main'
        ]
    }
)
