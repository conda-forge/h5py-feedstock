set HDF5_VERSION=%hdf5%
set HDF5_DIR="%LIBRARY_PREFIX%"

"%PYTHON%" -m pip install . --no-deps --ignore-installed --no-cache-dir -vv
if errorlevel 1 exit 1
