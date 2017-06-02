"%PYTHON%" setup.py configure --hdf5="%LIBRARY_PREFIX%"  --hdf5-version=1.8.18
if errorlevel 1 exit 1

"%PYTHON%" setup.py install --single-version-externally-managed --record record.txt
if errorlevel 1 exit 1
