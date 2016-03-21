all:
	pyinstaller run.py -n scimpy --additional-hooks-dir pyinstaller-hooks
	cp LICENSE* dist/scimpy/
