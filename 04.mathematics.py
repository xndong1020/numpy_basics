import numpy as np
import sys

a = np.array([1, 2, 3, 4])

a = a + 2

# [3 4 5 6]
print(a)

a -= 3
# [0 1 2 3]
print(a)

a *= 20
# [ 0 20 40 60]
print(a)

a = a / 10
# [0. 2. 4. 6.]
print(a)

a = np.sin(a)
# [ 0.          0.90929743 -0.7568025  -0.2794155 ]
print(a)

a = np.cos(a)
# [1.         0.61430028 0.72703513 0.9612168 ]
print(a)

# math on 2 np arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# [ 6  8 10 12]
print(a + b)

# But you can do math on 2 np arrays with different shapes
# ValueError: operands could not be broadcast together with shapes (4,) (3,)
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7])
# print(a + b)
