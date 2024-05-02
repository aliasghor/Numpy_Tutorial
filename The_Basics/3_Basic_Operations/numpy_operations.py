# Import the numpy package
import numpy as np

# Basic Mathematics operations on Numpy array

"""
    Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
"""

# Addition
vector1 = np.array([1,2,3,4])
vector2 = np.arange(4)

result = vector1 + vector2
print(result)

# Substraction
vector1 = np.array([5,1,2,3])
vector2 = np.array([1,2,1,4])

result = vector1 - vector2
print(result)

# Multiplication
vector1 = np.array([5,1,2,3])
vector2 = np.array([1,2,1,4])

result = vector1 * vector2
print(result)

# Divison
vector1 = np.array([5,1,2,3])
vector2 = np.array([1,2,1,4])

result = vector1 / vector2
print(result)

# Exponent
vector2 = np.arange(5)
vector2 = np.arange(5) ** 2
print(vector2)

"""
    The * (Multiplication) operator will result elementwise multiplication. To perform Matrix multiplication
    we can use the "@" or use the .dot() method
"""

# A bit of recap of previous elementwise multiplication
matrix1 = np.array([[5,6],[7,8]])
matrix2 = np.arange(4).reshape(2,2)
elementwise_multiplication = matrix1 * matrix2
print(elementwise_multiplication)

# To perform Matrix multiplication
matrix1 = np.array([[5,6],[7,8]])
matrix2 = np.arange(4).reshape(2,2)
matrix_multiplication = matrix1 @ matrix2
print(matrix_multiplication)

