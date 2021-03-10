import numpy as np
import sys

a = np.ones((2, 3))
"""
[[1. 1. 1.]
 [1. 1. 1.]]
"""
print(a)

b = np.full((3, 2), 2)
"""
[[2 2]
 [2 2]
 [2 2]]
"""
print(b)
# np has matrix multiply function
c = np.matmul(a, b)
"""
[[6. 6.]
 [6. 6.]]
"""
print(c)

# Find the determinant
d = np.identity(3)
# 1.0
print(np.linalg.det(d))
