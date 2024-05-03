import numpy as np

A = np.arange(1, 37)
A = A.reshape(3, 3, 4)
print(A)

print(A.shape, A.size)

A_r = A.reshape(3, 4, 3)
print(A_r)

A_f = A.flatten()
print(A_f)
