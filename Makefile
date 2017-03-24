all:
	pyinstaller run.py -n scimpy
	cp LICENSE* dist/scimpy/

clean:
	-rm -r scimpy.egg-info dist deb_dist __pycache__ build *~ scimpy/*~ scimpy/*.pyc
