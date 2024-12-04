import os

os.environ['OMPI_MCA_plm'] = 'isolated'
os.environ['OMPI_MCA_btl_vader_single_copy_mechanism'] = 'none'
os.environ['OMPI_MCA_rmaps_base_oversubscribe'] = 'yes'

import h5py
import h5py._conv
import h5py._errors
import h5py._objects
import h5py._proxy
import h5py.defs
import h5py.h5
import h5py.h5a
import h5py.h5d
import h5py.h5f
import h5py.h5fd
import h5py.h5g
import h5py.h5i
import h5py.h5l
import h5py.h5o
import h5py.h5p
import h5py.h5r
import h5py.h5s
import h5py.h5t
import h5py.h5z
import h5py.utils

# verify that mpi builds are built with mpi
should_have_mpi = os.getenv('mpi', 'nompi') != 'nompi'
have_mpi = h5py.get_config().mpi
assert have_mpi == should_have_mpi, "Expected mpi=%r, got %r" % (should_have_mpi, have_mpi)

from sys import exit
test_args = []
if have_mpi:
    test_args.append("--with-mpi")

# HDF5 1.14.4 and 1.14.5 have a regression in unicode handling on windows
# https://github.com/conda-forge/hdf5-feedstock/issues/240
# https://github.com/HDFGroup/hdf5/issues/5037
if (
    sys.platform == 'win32' and 
    h5py.h5.get_libversion() in [(1, 14, 4), (1, 14, 5)]
):
    test_args.extend(["-k", '"(not test_unicode_hdf5_python_consistent)"'])

exit(h5py.run_tests(" ".join(test_args)))
