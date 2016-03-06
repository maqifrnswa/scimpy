from setuptools import setup, find_packages
try:
    import py2exe
except:
    pass

setup(
    name = "scimpy",
    version = "0.0.dev1",
    packages = find_packages(),
    scripts = ['scimpy.py']
)
