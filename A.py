#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Define the potential energy function
def V(x, a, b, Vo):
    if x < 0 or x > b:
        return np.inf
    elif x < a:
        return 0
    else:
        return Vo

# Define the constants and parameters
hbar = 1
m = 1
N = 1000
a = 0
b = 1
Vo = 100

# Define the discretized grid
x = np.linspace(a, b, N)

# Define the step size
dx = x[1] - x[0]

# Define the potential energy array
V_array = np.array([V(xi, a, b, Vo) for xi in x])

# Define the kinetic energy operator
T = np.zeros((N, N))
for i in range(1, N - 1):
    T[i, i] = -2
    T[i, i + 1] = 1
    T[i, i - 1] = 1
T /= dx ** 2
T *= -hbar ** 2 / (2 * m)

# Solve for the eigenvalues and eigenvectors
E, psi = np.linalg.eigh(T + np.diag(V_array))

# Plot the results
plt.plot(x, psi[:, 0], label='Ground state')
plt.plot(x, psi[:, 1], label='First excited state')
plt.plot(x, psi[:, 2], label='Second excited state')
plt.xlabel('Position')
plt.ylabel('Wave function')
plt.legend()
plt.show()


# In[ ]:




