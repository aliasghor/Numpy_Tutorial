# Import the numpy package
import numpy as np

"""
    Here are some additional or useful (for those who think it is useful) array functions:
    - Function zeros() will create an array full of zeros
    - Function ones() will create an array full of ones
    - Function empty() will create an array whose initial content is random and depends on the state of the memory
    - Function arange() will create an array with a given specified range
    - Function linspace() will create an array evenly spaced numbers based on the argument
"""

# Function zeros()
print(20 * "=" + " Function zeros() " + 20 * "=")

# Create a Vector full of zeros
array_zeros = np.zeros(5) 
print(array_zeros)

# Create a Matrix full of zeros

# Create an array that has 2 axes. The first axis has a length of 3, the second axis has a length of 4
matrix_zeros = np.zeros((3,4))
print(matrix_zeros)

# Function ones()
print("\n" + 20 * "=" + " Function ones() " + 20 * "=")

# Create a Vector full of ones
array_ones = np.ones(5) 
print(array_ones)

# Create a Matrix full of ones

# Create an array that has 2 axes. The first axis has a length of 5, the second axis has a length of 3
matrix_ones = np.ones((5,3))
print(matrix_ones)

# Function empty()
print("\n" + 20 * "=" + " Function empty() " + 20 * "=")

# Create a Vector whose initial content is random and depends on the of the memory. By default the dtype is float64
vector_empty = np.empty(5)
print(vector_empty)

# Create a Matrix whose initial content is random and depends on the state of the memory. By default the dtype is float64
matrix_empty = np.empty((3,5))
print(matrix_empty)

# Function arange()
print("\n" + 20 * "=" + " Function arange() " + 20 * "=")

"""
    This will create a vector that holds a number starting from 0 until 4.
    The reason why it ends at number 4 is because 5 is excluded, whereas the
    start number is always included
"""
vector_num = np.arange(5)
print(vector_num)

tensor_num = np.arange(36).reshape(3,2,6)
print(tensor_num)


# Function linspace()

# Function linspace() will create an evenly spaced number array based on the argument

# Create an array starting from number 0 until 2 with a total elements of 9
array_linspace = np.linspace(0,2,9)
print(array_linspace)
