import numpy as np
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Sum of all elements :", arr.sum())
print("Sum of each column :", arr.sum(axis = 0))
print("Sum of each row :", arr.sum(axis = 1))
