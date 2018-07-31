from numpy import array, sqrt
from numpy.linalg import solve

m_disk = 2
m_bar = 3
radius_disk = 0.2
lenght_bar = 0.6
M = [-10, 10, 0]
I_bar = array([[0, 0, 0,],
               [0, 1, 0],
               [0, 0, 1] ]) * 1./12 * m_bar * lenght_bar**2
I_bar_displacement = array([[0, 0, 0],
                            [0, 0.2**2, 0],
                            [0, 0, 0.2**2]]) * m_bar
I_disk = array([[1./4, 0, 0],
                [0, 1./4, 0],
                [0, 0, 1./2]]) * m_disk * radius_disk**2
I_disk_displacement = array([[0, 0, 0],
                             [0, 0.3**2, 0],
                             [0, 0, 0.3**2]]) * m_disk
I = I_bar + I_bar_displacement + I_disk + I_disk_displacement
I = array([[I[0, 0], -I[0, 1], -I[0, 2]],
           [-I[1, 0], I[1, 1], -I[1, 2]],
           [-I[2, 0], -I[2, 1], I[2, 2]]])
alpha = solve(I, M)
print('Angular acceleration is: ', alpha)
print("Magnitude of angular acceleration is: ", sqrt(alpha.dot(alpha)))