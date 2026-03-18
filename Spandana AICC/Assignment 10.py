import time
import numpy as np

# 1. Create 1 million numbers using Python list
size = 1_000_000
py_list = list(range(size))

# 2. Create 1 million numbers using NumPy array
np_array = np.arange(size)

# -----------------------------
# Time addition in Python list
# -----------------------------
start_time = time.time()
py_list_sum = [x + 10 for x in py_list]  # Add 10 to each element
end_time = time.time()
list_time = end_time - start_time
print(f"Python list operation time: {list_time:.5f} seconds")

# -----------------------------
# Time addition in NumPy array
# -----------------------------
start_time = time.time()
np_array_sum = np_array + 10  # Vectorized addition
end_time = time.time()
numpy_time = end_time - start_time
print(f"NumPy array operation time: {numpy_time:.5f} seconds")

# -----------------------------
# Observations
# -----------------------------
print("\n--- Observations ---")
print("1. NumPy operations are significantly faster than Python list operations for large data.")
print("2. NumPy uses vectorized operations which avoid explicit Python loops, saving time.")
print("3. NumPy arrays consume less memory and are optimized for numerical computations.")