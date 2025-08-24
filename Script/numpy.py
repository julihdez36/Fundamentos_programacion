import numpy as np

print(np.__version__)

# Creating Arrays from Python Lists

# integer array:
np.array([1, 4, 2, 5, 3])

# NumPy is constrained to arrays that all contain the same type
np.array([3.14, 4, 2, 3])

# If we want to explicitly set the data type of the resulting array
np.array([1, 2, 3, 4], dtype='float32')

# We can create an array from list comprehension

np.array([i for i in range(2,10,2)])

# nested lists result in multi-dimensional arrays

np.array([range(i, i + 3) for i in [2, 4, 6]])


# Creating Arrays from Scratch ----------------------------------------

# Especially for larger arrays, it is more efficient to create arrays from scratch
 # using routines built into NumPy

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with ones
np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0, 20, 2)


# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3, 3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0, 10, (3, 3))


# Create a 3x3 identity matrix
np.eye(3)

# NumPy Array Attributes -------------------------------------------

np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

# Each array has attributes ndim (the number of dimensions), 
# shape (the size of each dimension), and size (the total size of the array)
    
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)

print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")


# Array Indexing: Accessing Single Elements ----------------------------

x1
x1[0], x1[4]

# To index from the end of the array, you can use negative indices

x2
x2[0, 0], x2[2, 0], x2[2, -1]


x1[-1], x1[-2]

# Values can also be modified using any of the above index notation

x2[0, 0] = 12
x2

# Array Slicing: Accessing Subarrays -------------------------------------


# https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html