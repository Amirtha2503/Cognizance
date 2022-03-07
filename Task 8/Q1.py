# Amirthavarshini V (21105)
# Question - 1
# Consider the vector [10, 11, 12, 13, 14], build a new vector with 5 consecutive zeros between each value?

import numpy as np
A = np.array([10,11,12,13,14])
na = 5
A0 = np.zeros(len(A) + (len(A)-1)*(na))
A0[::na+1] = A
print(A0)
