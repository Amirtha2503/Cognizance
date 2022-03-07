# Amirthavarshini V (21105)
# Question - 2
# Consider two random array A anb B, check if they are equal

import numpy as np
arr1 = np.random.randint(0,10,10)
print("Array 1 :")
print(arr1)
arr2 = np.random.randint(0,10,10)
print("Array 2 :")
print(arr2)
arr3 = np.allclose(arr1, arr2)
print(arr3)
