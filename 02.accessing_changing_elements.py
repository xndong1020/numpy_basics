import numpy as np
import sys

# a 2 by 7 array
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# (2, 7)
print(a.shape)

# Get a specific element [r, c], meaning [rowIndex, columnIndex]
# 13, the second row, sixth column
print(a[1, 5])

# Select from right
# 13, the second row, second from right
print(a[1, -2])

# Get a specific row
# [1 2 3 4 5 6 7]
print(a[0])

# Get a specific row
# [1 2 3 4 5 6 7]
print(a[0, :])

# Get a specific column
# [ 7 14]
print(a[:, -1])  # to get last column

# Get a block
"""
[ 7 14]
[[6 7]]
"""
print(a[:1, 5:])  # up to 2nd row, and from the sixth column

# Get a block, with steps
"""
[[ 1  3  5]
 [ 8 10 12]]
"""
print(
    a[:, :5:2]
)  # all rows, starts from the first column, ends at the sixth column, with step of 2.


# Changing value is straight forward
a[1, 5] = 2000
"""
[[   1    2    3    4    5    6    7]
 [   8    9   10   11   12 2000   14]]
"""
print(a)

# change entire row
"""
[[   5    5    5    5    5    5    5]
 [   8    9   10   11   12 2000   14]]
"""
a[0, :] = 5
print(a)
