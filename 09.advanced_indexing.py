import numpy as np
import sys


# you can index with a list in numpy
a = np.array([1, 2, 3, 4, 5])
# [1 3 5]
print(a[[0, 2, 4]])

a = np.genfromtxt("./data.csv", delimiter=",")

"""
[[False False False False  True  True False False False False False False
  False False False False False False]
 [False False False False  True  True False  True False False False False
  False False False False False False]
 [False False False False  True False False False  True False False False
  False False False False  True  True]]
"""
# boolean masking/filtering
print(a > 50)

# advance index to keep any numbers > 50
"""
[196.  75. 766.  75.  55. 999.  78.  76.  88.]
"""
print(a[a > 50])

# multiple conditions
# [75. 75. 55. 78. 76. 88.]
print(a[(a > 50) & (a < 100)])

# Not operator '~'
"""
[  1.  13.  21.  11. 196.   4.   3.  34.   6.   7.   8.   0.   1.   2.
   3.   4.   5.   3.  42.  12.  33. 766.   4.   6.   4.   3.   4.   5.
   6.   7.   0.  11.  12.   1.  22.  33.  11. 999.  11.   2.   1.   0.
   1.   2.   9.   8.   7.   1.]
"""
print(a[~((a > 50) & (a < 100))])

# to check if any lines(rows) has value greater than 50
# [ True  True  True]
print(np.any(a > 50, axis=1))

