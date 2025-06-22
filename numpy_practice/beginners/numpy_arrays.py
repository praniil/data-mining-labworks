import numpy as np

#1.	Create a 1D NumPy array with values from 0 to 9.
oned_array = np.arange(0, 10, 1)
print(oned_array)

#2.	Create a 3x3 NumPy array of all zeros.
three_by_three = np.zeros((3, 3))
print(three_by_three)

#3.	Create a 5x5 identity matrix.
five_by_five_identity = np.identity(5)
print(five_by_five_identity)

#4.	Create a 4x4 matrix with random integers between 10 and 50.
array1 = np.random.randint(10, 51, (4, 4))
print(array1)

#5.	Get the shape, size, and data type of a NumPy array.
print(array1.shape)
print(array1.size)
print(array1.dtype)

#6.	Reshape a 1D array of size 12 into a 3x4 matrix.
oned = np.random.randint(0, 10, (1, 12))
print(oned)
reshaped_oned = oned.reshape(3, 4)
print(reshaped_oned)

#7.	Access and modify the center element of a 3x3 array.
threeD = np.array([[1, 26, 3], [1, 2, 3], [3, 4, 5]])
print(threeD)

center_element = threeD[1][1]
print(center_element)

threeD[1][1] = 66
center_element = threeD[1][1]
print(center_element)