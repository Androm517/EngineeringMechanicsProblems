from numpy import array
from numpy.linalg import solve

I = [[1./2, -2./3, 0], [-2./3, 8./3, 0], [0, 0, 167./999]]
M = [0, 0, -1200]
I = array(I)
M = array(M)
print('angular acceleration alpha is: ', solve(I, M))
