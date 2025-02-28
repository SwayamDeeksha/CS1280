import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print("Original Array:\n", arr)

# Slicing every second row and column
sliced_arr = arr[::2, ::2]

# Slice the first row
row_slice = arr[0, :] # Equivalent to arr[0]

# Slice the second column
col_slice = arr[:, 1]

# Slice a submatrix (rows 1-2, columns 2-3)
submatrix = arr[1:3, 2:4]

print("\nSliced Array with Steps:\n", sliced_arr)
print("First Row:", row_slice)
print("Second Column:", col_slice)
print("Submatrix:\n", submatrix)