from numpy import array, cross, sqrt
from numpy.linalg import solve


m = 20
h = 0.4
b = 0.6
F = array([0., 10., 0.])
r_F = array([b, 0, -h]) * 0.5
r_A = array([-b, 0, h]) * 0.5
M = cross(r_F, F)
acc_CM = F / m
I = array([[h**2, 0, 0], [0, b**2 + h**2 , 0], [0, 0, b**2]]) * 1/12. * m
alpha = solve(I, M)
acc_A = acc_CM + cross(alpha, r_A)
abs_acc_A = sqrt(acc_A.dot(acc_A))
print('acceleration of point A is:')
print(abs_acc_A)