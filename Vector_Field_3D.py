import numpy as np
import matplotlib.pyplot as plt
import math

# Define the vector-valued function in 3D
def vector_field_3d(x, y, z):

    r_square = x**2+y**2
    u1x = -y
    u2y = x
    u3z = z
    return u1x, u2y, u3z

ax = plt.figure().add_subplot(projection='3d')

# Plot range
n = 3

x = np.linspace(-n, n, 5)
y = np.linspace(-n, n, 5)
z = np.linspace(-n, n, 5)
X, Y, Z = np.meshgrid(x, y, z)

U1, U2, U3 = vector_field_3d(X, Y, Z)

ax.quiver(X, Y, Z, U1, U2, U3)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Vector field')
plt.grid(True)
plt.show()
