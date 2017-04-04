"%PYTHON%" setup.py configure --hdf5="%LIBRARY_PREFIX%"
if errorlevel 1 exit 1

"%PYTHON%" setup.py install --single-version-externally-managed --record record.txt --hdf5-version=1.8.17
if errorlevel 1 exit 1
