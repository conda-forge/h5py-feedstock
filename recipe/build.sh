#!/bin/bash

export HDF5_VERSION=${hdf5}
export HDF5_DIR=${PREFIX}
export OPAL_PREFIX=${PREFIX}
if [[ "$mpi" != "nompi" ]]; then
  export HDF5_MPI="ON"
fi

if [[ ${target_platform} == "osx-arm64" ]]; then
  export CIBW_ARCHS_MACOS=arm64
fi

# tell setup.py to not 'pip install' exact package requirements
export H5PY_SETUP_REQUIRES="0"

"${PYTHON}" -m pip install . --no-deps --ignore-installed --no-cache-dir -vv
