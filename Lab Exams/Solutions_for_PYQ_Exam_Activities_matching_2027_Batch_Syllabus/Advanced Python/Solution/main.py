import numpy as np
import matplotlib.pyplot as plt
import time
"""
Import vectorized() and nonvectorized() from operation.py
Use the testcases given in the folder testcases to test your code here. You can print the result to check if it is correct.
"""
from operation import nonvectorized, vectorized

"""
Read the values from data/nonvectorized.txt and data/vectorized.txt into separate lists
Read values as float values.
"""
file = open("data/nonvectorized.txt", "r")
nonvectorized_list = []
for line in file.readlines():
    nonvectorized_list.append((float)(line))
file.close()
file = open("data/vectorized.txt", "r")
vectorized_list = []
for line in file.readlines():
    vectorized_list.append((float)(line))
file.close()
N = np.arange(100)
N_2 = N**2
N_3 = N**3
N_scaled = N/1e6
N_2_scaled = N_2/1e6
N_3_scaled = N_3/1e6
plt.figure(figsize=(10,6)) # Don't change this line

"""
Draw a plot as specified in the problem statment using above values
"""
plt.plot(N, nonvectorized_list, label="Non-vectorized")
plt.plot(N, vectorized_list, color = 'orange', label="Vectorized")
plt.plot(N, N_scaled, 'g', linestyle='dashed', label="N")
plt.plot(N, N_2_scaled, 'r', linestyle='dashed', label="N^2")
plt.plot(N, N_3_scaled, color = 'purple', linestyle='dashed', label="N^3")
plt.xlabel("Input size N")
plt.ylabel("Execution time (s)")
plt.legend()
# save your plot in the end
plt.savefig('plot.png')
