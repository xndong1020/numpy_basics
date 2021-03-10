import numpy as np
import sys

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# before is (2,4), we want to reshape it to (4,2)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
after = before.reshape((4, 2))
print(after)

# vstack - vertically stack arrays
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
"""
[[1 2 3 4]
 [5 6 7 8]
 [5 6 7 8]
 [1 2 3 4]]
"""
print(np.vstack([v1, v2, v2, v1]))

# hstack - horizontally stack arrays
"""
[[1. 1. 1. 1]
 [1. 1. 1. 1]]
"""
h1 = np.ones((2,4))
"""
[[0. 0.]
 [0. 0.]]
"""
h2 = np.zeros((2,2))
"""
[[1. 1. 1. 1. 0. 0.]
 [1. 1. 1. 1. 0. 0.]]
"""
print(np.hstack([h1, h2]))
