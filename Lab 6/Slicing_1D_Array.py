import numpy as np

arr = np.arange(10)
print("Original array:", arr) # Original array: [0 1 2 3 4 5 6 7 8 9]
print("Element at index 5:", arr[5]) # Element at index 5: 5
print("Slice from index 5 to 8:", arr[5:8]) # Slice from index 5 to 8: [5 6 7]
arr[5:8] = 12
print("Modified array:", arr) # Modified array: [ 0 1 2 3 4 12 12 12 8 9]