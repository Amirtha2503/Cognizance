# Amirthavarshini V (21105)
# Question - 5
# Do any two Exercises using Numpy

# 7) Getting the indexes where elements of 2 numpy arrays match

import numpy as np
arr1 = np.array([12,14,56,78,43,21])
arr2 = np.array([12,23,56,45,267,21])
print([x for x, y in enumerate(arr1) if y in set(arr2)])
