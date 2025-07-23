import numpy as np

# a[:, np.newaxis]
#  it turns the row vector into a column vector

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
a[:, np.newaxis] + b

# a[:, np.newaxis] = 
# [[ 0.0],
#  [10.0],
#  [20.0],
#  [30.0]]

# a[:, np.newaxis] has shape (4, 1)
# b has shape (3,) → it is broadcasted to shape (1, 3)

# So NumPy broadcasts both arrays to shape (4, 3) and performs element-wise addition.

# a[:, np.newaxis] + b =
# [[ 0. + 1.,  0. + 2.,  0. + 3.],     → [ 1.,  2.,  3.]
#  [10. + 1., 10. + 2., 10. + 3.],     → [11., 12., 13.]
#  [20. + 1., 20. + 2., 20. + 3.],     → [21., 22., 23.]
#  [30. + 1., 30. + 2., 30. + 3.]]     → [31., 32., 33.]
