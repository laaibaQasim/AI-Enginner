# how to reverse a numpy array
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.flip(a))
# [[8 7 6 5]
#  [4 3 2 1]]

#  for 3d array
b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(np.flip(b, axis=0))

# np.flip(a, axis=0) → Flips blocks
# np.flip(a, axis=1) → Flips rows within each block
# np.flip(a, axis=2) → Flips columns in each row

# how to we find unique elements, their counts, unique rows, and unique columns
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
print(unique_values)
# [11 12 13 14 15 16 17 18 19 20]

unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)
# [ 0  2  3  4  5  6  7 12 13 14]

unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)
# [3 2 2 2 1 1 1 1 1 1]

#  for 2D array
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_values = np.unique(a_2d)
print(unique_values)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

unique_rows, indices, occurrence_count = np.unique(
    a_2d, axis=0, return_counts=True, return_index=True
)
print(unique_rows)
print(indices)
print(occurrence_count)
