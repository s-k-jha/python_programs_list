import numpy as np 
from math import sin 

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])

for x in np.nditer(arr1):
 print(sin(x))