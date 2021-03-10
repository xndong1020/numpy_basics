import numpy as np
import sys

# Create an array.
# numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
a = np.array([1, 2, 3], dtype="int8")

# [1 2 3]
print(a)

# 2 dimensions
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# [[1. 2. 3.]
# [4. 5. 6.]]
print(b)

# Get dimension of array
# Dimension 1 2
print("Dimension", a.ndim, b.ndim)

# Get shape of array
# Shape (3,) (2, 3), because a is 1 dimensional, b has 2 rows and 3 cols
print("Shape", a.shape, b.shape)

# Get Type/Size
# Type int8 size 1 byte
print("Type", a.dtype, "size", a.itemsize)

# Type float64, size 8 bytes
print("Type", b.dtype, "size", b.itemsize)

# Get total size (how many elements in total)
# size 3
print("size", a.size)
# size 6
print("size", b.size)

# Get total itemsize (how big the elements in total)
# size 3
print("size", a.nbytes)
# size 48, because float is 8 bytes
print("size", b.nbytes)

