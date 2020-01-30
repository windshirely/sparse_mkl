# sparse_dot_mkl

This is a wrapper for the sparse matrix multiplication in the intel MKL library.
It is implemented entirely in native python using `ctypes`.
The main advantage to MKL (which motivated this) is multithreaded sparse matrix multiplication. 
The scipy sparse implementation is single-threaded at the time of writing (2020-01-03).
A secondary advantage is the direct multiplication of a sparse and a dense matrix without requiring any
intermediate conversion (also multithreaded). 

The only function explicitly available is `dot_product_mkl`, which takes two matrices
`dot_product_mkl(A, B)` and a matrix that is `A (dot) B`. 
If both matrices are dense, the output will be dense.
If one matrix is dense and one is sparse, the output will be dense.
If both matrices are sparse, the output will be sparse unless the `dense=True` flag is passed.
The dense flag will directly multiply to a dense matrix without requiring intermediate conversion.
It has no effect if set when a dense output would normally be produced.

If both matrices are sparse, they must be of the same type (CSC or CSR).
If one matrix is sparse, it is more efficient if it is CSR, but CSC will work.
There is no support currently for COO or BSR sparse matrices. 
Numpy (dense) arrays must be C-ordered and contiguous (these are the defaults in most situations).

This only does floating point data, and both matrices must be identical types.
If `cast=True` non-float matrices will be converted to doubles,
and a single-precision matrix will be promoted to doubles unless both matrices are single-precision. 
`cast=True` will ***not*** change data in-place, but will instead make an internal copy. 
This function may also reorder sparse data structures without warning while creating MKL's internal matrix representation.

This package requires `libmkl_rt.so`. This is distributed with the full version of conda,
and can be installed into Miniconda with `conda install -c intel mkl`.
Alternatively, you may add need to add the path to MKL shared objects to `LD_LIBRARY_PATH`
(e.g. `export LD_LIBRARY_PATH=/opt/intel/mkl/lib/intel64:$LD_LIBRARY_PATH`).
There are some known bugs in MKL v2019 which may cause intermittent segfaults.
Updating to MKL v2020 is highly recommended if you encounter any problems.