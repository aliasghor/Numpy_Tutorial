# Import the numpy package
import numpy as np

# This explanations file may be redundant to the previous directory file. But it is generally good to keep practicing.

"""
    Here are the algorithms (set of step-by-step instructions) to create an array:
    - to create an array we first have to used the array function()
    - We can use the built in data structures like a List or Tuple to pass to the argument
"""

# Create a Vector (1D array)
vector = np.array([1,2,3,4,5],dtype=np.int16) # Specified the array data type using the keyword argument dtype
print(vector)
print(f"Vector has a length for about = {vector.size}")
print(f"Vector array holds each element data type of = {vector.dtype}")
print(f"In each element of vector stores a memory size for about = {vector.itemsize} Bytes")
print(f"Total memory consumption of vector array is = {vector.nbytes} Bytes")

# Create a Matrices (2D array) or array that has 2 axes

# There are two ways that we can define a Matrices:

# First is use list and then proceed with tuples
# matrix = np.array([(1,2,3),(4,5,6)])

# Second is use the list again but proceed with list. It is like a list within a list
matrix = np.array([[1,2,3],[4,5,6]])

# Either way both are correct to create a Matrix

# Print out the result
print(matrix)
print(f"Matrix has an axes for about = {matrix.ndim} axes")
print(f"Each element in matrix axis has a data type of = {matrix.dtype}")
print(f"Matrix has a rows and columns for about = {matrix.shape}")
print(f"Each element inside a Matrix axis holds a memory for about = {matrix.itemsize} Bytes")
print(f"Matrix consumed a memory size for about = {matrix.nbytes} Bytes")

# Creating a tensor (3D array) or an array that has 3 axes. Tensor is often considered as a list of Matrices

# Creating a tensor that has 3 rows, and each Matrices has 2 rows and 6 columns. The reshape numbers must be equivalent to the product of total arange number
tensor = np.arange(36).reshape(3,2,6) 
print(tensor)