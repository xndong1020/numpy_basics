import numpy as np
import sys

# init array with 0s
"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""
a = np.zeros((2, 3))
print(a)

# init array with 1s
"""
[[1 1]
 [1 1]
 [1 1]
 [1 1]]
"""
a = np.ones((4, 2), dtype="int8")
print(a)

# init array with any number
"""
[[99 99 99]
 [99 99 99]]
"""
a = np.full((2, 3), 99)
print(a)

# init array with any number, using the shape of an existing np array
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# (2, 5)
print(b.shape)
"""
[[100 100 100 100 100]
 [100 100 100 100 100]]
"""
a = np.full(b.shape, 100)
print(a)

# init array with random decimal numbers
"""
[[0.78049648 0.26356169]
 [0.46088537 0.92474463]
 [0.15290645 0.61598542]
 [0.03420792 0.784052  ]]
"""
a = np.random.rand(4, 2)
print(a)

# init array with random decimal numbers, using the shape of an existing np array
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
"""
[[0.87825252 0.72141859]
 [0.8723718  0.76555121]
 [0.33980731 0.72665856]
 [0.43332843 0.00246865]]
"""
a = np.random.random_sample(a.shape)
print(a)

# random integer values, between the range 4-7 (include 4 but exclude 7)
"""
[[4 4 6]
 [6 4 6]
 [5 6 4]]
"""
a = np.random.randint(4, 7, size=(3, 3))
print(a)


# repeat an existing np array
b = np.array([[1, 2, 3]])
"""
[1 1 1 2 2 2 3 3 3]
"""
a = np.repeat(b, 3)
print(a)

# “axis 0” represents rows and “axis 1” represents columns.
"""
[[1 2 3]
 [1 2 3]
 [1 2 3]]
"""
a = np.repeat(b, 3, axis=0)  # repeat along row direction
print(a)

"""
[[1 1 1 2 2 2 3 3 3]]
"""
a = np.repeat(b, 3, axis=1)  # repeat along column direction
print(a)


# quiz

init = np.full((5, 5), 1)
"""
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
"""
print(init)

inner = np.full((3, 3), 0)
"""
[[0 0 0]
 [0 0 0]
 [0 0 0]]
"""
print(inner)

inner[1, 1] = 9
"""
[[0 0 0]
 [0 9 0]
 [0 0 0]]
"""
print(inner)

init[1:-1, 1:-1] = inner
"""
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
"""
print(init)

### Be careful when copying arrays!!!
a = np.array([1, 2, 3])
b = a  # a direct copy

# to make a new copy, using copy function
c = a.copy()

b[0] = 100  # you though you are changing the value in b
c[-1] = 200  # c will NOT have the same issue

# [100   2   3]
print(a)  # but value in a also changed

