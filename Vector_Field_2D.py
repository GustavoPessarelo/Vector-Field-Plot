import numpy as np
import matplotlib.pyplot as plt
import math

# Define the vector-valued function in 2D
def vector_field(x, y):
    r = np.sqrt(x**2+y**2)
    u1x = X + x/r
    u2y = y/r

    return u1x, u2y

n = 3

x = np.linspace(-n, n, 10)
y = np.linspace(-n, n, 10)
X, Y = np.meshgrid(x, y)

U1, U2 = vector_field(X, Y)

plt.quiver(X, Y, U1, U2)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Campo vetorial')
plt.grid(True)
plt.show()
