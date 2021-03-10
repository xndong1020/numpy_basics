import numpy as np
import sys

stats = np.array([[1, 2, 3], [4, 5, 6]])
"""
[[1 2 3]
 [4 5 6]]
"""
print(stats)
# 1
print(np.min(stats))
# [1 2 3], because row [1,2,3] < row [4,5,6]
print(np.min(stats, axis=0))  # get min on row basis
# [1 4], because in the 2 arrays, the min values are [1, 4]
print(np.min(stats, axis=1))  # get min on column basis

# 6
print(np.max(stats))

# 3.5
print(np.mean(stats))

# 21
print(np.sum(stats))
# [5 7 9]
print(np.sum(stats, axis=0))
# [ 6 15]
print(np.sum(stats, axis=1))
