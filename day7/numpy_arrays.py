# numpy_arrays.py
# Demonstrates NumPy array creation, inspection, indexing, and slicing

import numpy as np

# Create arrays
arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.arange(1, 11)

arr3 = np.zeros((2, 3))

arr4 = np.linspace(0, 100, 5)

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nArray 3:")
print(arr3)

print("\nArray 4:")
print(arr4)

# Inspect arrays
print("\nArray Information")

print("\narr1:")
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)
print("Dimensions:", arr1.ndim)

print("\narr3:")
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
print("Dimensions:", arr3.ndim)

# Indexing
print("\nIndexing Examples")

print("First element:", arr2[0])

print("Last element (negative index):", arr2[-1])

# Slicing
print("\nSlicing Examples")

print("Elements from index 2 to 6:")
print(arr2[2:7])

print("\nSubarray:")
print(arr2[4:9])