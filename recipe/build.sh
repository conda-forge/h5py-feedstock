set -ex

export HDF5_VERSION=${hdf5}
if [[ "$CONDA_BUILD_CROSS_COMPILATION" == "1" ]]; then
  # load HDF5 library from _build_env
  export HDF5_DIR=${BUILD_PREFIX}
else
  export HDF5_DIR=${PREFIX}
fi
export OPAL_PREFIX=${PREFIX}
if [[ "$mpi" != "nompi" ]]; then
  export HDF5_MPI="ON"
fi

# tell setup.py to not 'pip install' exact package requirements
export H5PY_SETUP_REQUIRES="0"

"${PYTHON}" -m pip install . --no-deps --ignore-installed --no-cache-dir -vv
