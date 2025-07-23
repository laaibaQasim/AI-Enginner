import numpy as np

a = np.full((5, 5), 1)
a[a < 0] = 0
print(a)

print(
    np.sum(a, axis=0)
)  # axis=0 means “along the rows”, but what it actually returns is per-column values, because rows are being collapsed.

sums = np.sum(a, axis=0)

print(
    np.where(a < sums, 1, 0)
)  # Here sums will be broadcasted to match the shape of a, and the comparison will be done element-wise.
