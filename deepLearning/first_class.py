# print("hello world")
import numpy as np
import matplotlib.pyplot as plt

# v1 = np.array([[2, 5, 4, 7]])
# print(v1)
# v2 = v1.T
# print(v2)

# print()
# v1 = np.array([2, 5, 4, 7])
# v2 = np.array([4, 1, 0, 2])
# v3 = np.dot(v1, v2)
# print(v3)

# # scalars values
# l1 = 1
# l2 = 2
# l3 = -3

# # vector values
# v1 = np.array([4, 5, 1])
# v2 = np.array([-4, 0, -4])
# v3 = np.array([1, 2, 3])

# # linear regression
# v4 = l1*v1 + l2*v2 + l3*v3
# print(v4)


# v1 = np.array([2, 5, 4, 7])
# v2 = np.array([4, 1, 0, 2])
# op = np.outer(v1, v2)
# normalProduct = np.dot(v1, v2)
# print(op)
# print(normalProduct)


v = np.array([2, 5, 4, 7])
# it's norm
vMag = np.linalg.norm(v)
v_unit = v / vMag
print(v_unit)

