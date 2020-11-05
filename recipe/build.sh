#!/bin/bash

export HDF5_DIR=${PREFIX}
if [[ "$mpi" != "nompi" ]]; then
  export HDF5_MPI="ON"
fi

"${PYTHON}" -m pip install . --no-deps --ignore-installed --no-cache-dir -vv
