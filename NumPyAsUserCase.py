import numpy as np
import time
import sys
import os

# --- NumPy Array Basics ---
# The core of NumPy is the ndarray object, which offers significant advantages over Python lists for numerical tasks.

# 1. Creating NumPy Arrays
# ADVANTAGE 1: Homogeneous Data Type - NumPy arrays store elements of a single, fixed data type.
# This allows for more efficient memory storage and faster computations.
my_list = [1, 2, 3, 4, 5]
np_array_from_list = np.array(my_list)
print(f"Array from list: {np_array_from_list}")
print(f"Type: {type(np_array_from_list)}")
print(f"Shape: {np_array_from_list.shape}")
print(f"Data type of elements: {np_array_from_list.dtype}\n") # Notice the single dtype (e.g., int32 or int64)

# ADVANTAGE 2: Multi-dimensional Arrays - NumPy natively supports N-dimensional arrays,
# making it ideal for matrices, images, and other multi-dimensional data without complex nesting.
nested_list = [[1, 2, 3], [4, 5, 6]]
np_2d_array = np.array(nested_list)
print(f"2D array from nested list:\n{np_2d_array}")
print(f"Shape: {np_2d_array.shape}")
print(f"Number of dimensions: {np_2d_array.ndim}\n")

# Creating arrays with specific values
zeros_array = np.zeros((3, 4))
ones_array = np.ones((2, 2))
full_array = np.full((2, 3), 7)
identity_matrix = np.eye(3)
arange_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 10, 5)
random_int_array = np.random.randint(0, 10, size=(2, 3))
random_float_array = np.random.rand(2, 3)

# --- Basic Array Operations ---
# ADVANTAGE 3: Vectorization (Speed/Performance) - NumPy operations are "vectorized."
# This means operations are applied to entire arrays at once, handled by highly optimized C/Fortran code,
# making them significantly faster than Python's interpreted loops for numerical tasks.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(f"arr1 + arr2: {arr1 + arr2}") # Element-wise addition
print(f"arr1 * 2: {arr1 * 2}\n")     # Scalar multiplication

# Matrix multiplication - intuitive and efficient
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(f"Matrix multiplication (dot product):\n{matrix1 @ matrix2}\n")

# ADVANTAGE 4: Rich Mathematical Functions (UFuncs) - NumPy provides a vast collection of
# universal functions (ufuncs) for performing common mathematical operations directly on arrays.
print(f"Square root of arr1: {np.sqrt(arr1)}")
print(f"Exponential of arr1: {np.exp(arr1)}\n")

# Aggregation functions (sum, mean, max, min, etc.) are also optimized
print(f"Sum of arr1: {np.sum(arr1)}")
print(f"Mean of arr1: {np.mean(arr1)}\n")

# --- Indexing and Slicing ---
# Similar to Python lists, but extended for N-dimensional arrays
arr = np.array([10, 20, 30, 40, 50, 60, 70])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"First element: {arr[0]}")
print(f"Elements from index 1 to 4: {arr[1:5]}")
print(f"Element at row 0, column 1: {matrix[0, 1]}")
print(f"Second column:\n{matrix[:, 1]}\n")

# ADVANTAGE 5: Powerful Boolean and Fancy Indexing - Easily filter or select elements
# based on conditions or arbitrary index arrays, leading to concise and readable code.
print(f"Elements greater than 50: {arr[arr > 50]}")
indices = [0, 2, 4]
print(f"Elements at specific indices {indices}: {arr[indices]}\n")

# --- Performance and Memory Efficiency Comparison ---
print("--- Performance & Memory Comparison (NumPy vs. Python List) ---")

size = 1000000

# Python List Performance
list1 = list(range(size))
list2 = list(range(size))

start_time = time.time()
result_list = [a + b for a, b in zip(list1, list2)]
end_time = time.time()
# Python list operations involve overhead due to iterating in Python and
# each element being a separate Python object with its own type, ref count etc.
print(f"Python list addition took: {end_time - start_time:.4f} seconds (slower due to Python loops and object overhead)")

# NumPy Array Performance
np_array1 = np.arange(size)
np_array2 = np.arange(size)

start_time = time.time()
result_numpy = np_array1 + np_array2 # Vectorized operation, executed in optimized C code
end_time = time.time()
# ADVANTAGE 1 (Performance/Speed): NumPy operations are implemented in highly optimized C/Fortran,
# leading to significantly faster execution for numerical tasks, especially on large datasets.
print(f"NumPy array addition took: {end_time - start_time:.4f} seconds (much faster due to vectorization)")

# Memory Efficiency
num_elements = 10000

# Python List Memory
py_list = list(range(num_elements))
# sys.getsizeof(py_list) gives the size of the list object itself (pointers)
# Each integer also consumes memory as a separate Python object
print(f"Size of Python list object (pointers only) for {num_elements} ints: {sys.getsizeof(py_list)} bytes")
print(f"Approximate total size (list object + {num_elements} int objects): {sys.getsizeof(py_list) + num_elements * sys.getsizeof(py_list[0])} bytes")

# NumPy Array Memory
np_array = np.arange(num_elements)
# ADVANTAGE 6 (Memory Efficiency): NumPy arrays store elements of a uniform type contiguously in memory,
# without the overhead of individual Python object headers or pointers for each element. This saves a lot of memory.
print(f"Size of NumPy array for {num_elements} ints: {sys.getsizeof(np_array)} bytes (much more memory efficient)\n")

# --- Reading Data from Files ---
print("--- Reading/Writing Data from Files ---")

# Create dummy CSV files for demonstration
with open('data.csv', 'w') as f:
    f.write('1,2,3\n4,5,6\n7,8,9\n')

with open('mixed_data.csv', 'w') as f:
    f.write('Name,Age,Score\n')
    f.write('Alice,25,88.5\n')
    f.write('Bob,,92.0\n')
    f.write('Charlie,30,\n')
    f.write('David,22,78.2\n')

# np.loadtxt is good for simple, purely numeric files
try:
    data = np.loadtxt('data.csv', delimiter=',')
    print(f"Data from data.csv:\n{data}\n")
except Exception as e:
    print(f"Error reading data.csv: {e}")

# np.genfromtxt is more robust for mixed data types, headers, and missing values
try:
    mixed_data = np.genfromtxt(
        'mixed_data.csv',
        delimiter=',',
        skip_header=1,
        dtype=None,
        encoding=None,
        names=['Name', 'Age', 'Score']
    )
    print(f"Data from mixed_data.csv:\n{mixed_data}")
    # ADVANTAGE 7: Seamless Integration with Scientific Libraries and Data Handling.
    # Functions like genfromtxt make it easy to load structured data, and
    # NumPy is the foundation for Pandas, SciPy, Scikit-learn, etc.
    print(f"Scores: {mixed_data['Score']}\n")
except Exception as e:
    print(f"Error reading mixed_data.csv: {e}")

# --- Saving Data to Files ---
my_array_to_save = np.array([[10, 20, 30], [40, 50, 60]])

# Saving to a text file (e.g., CSV)
np.savetxt('output_data.csv', my_array_to_save, delimiter=',', fmt='%d')
print("Array saved to 'output_data.csv'")

# Saving to NumPy binary format (.npy) - highly efficient for large arrays
np.save('my_array.npy', my_array_to_save)
print("Array saved to 'my_array.npy'")

# Cleaning up dummy files
os.remove('data.csv')
os.remove('mixed_data.csv')
os.remove('output_data.csv')
os.remove('my_array.npy')
print("\nDummy files removed.")