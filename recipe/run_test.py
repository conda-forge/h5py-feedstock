import os
import sys
import sysconfig

os.environ['AWS_REGION'] = 'us-east-2'
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

have_mpi = h5py.get_config().mpi

test_args = []
if have_mpi:
    test_args.append("--with-mpi")

# Build list of tests to skip
skip_tests = []

# Skip test_multiprocess on free-threading builds
is_freethreaded = bool(sysconfig.get_config_var("Py_GIL_DISABLED"))
if is_freethreaded:
    skip_tests.append("test_multiprocess")

# Apply test skip filter if any tests should be skipped
if skip_tests:
    skip_expr = " and ".join(f"not {test}" for test in skip_tests)
    test_args.extend(["-k", f'"{skip_expr}"'])

sys.exit(h5py.run_tests(" ".join(test_args)))
