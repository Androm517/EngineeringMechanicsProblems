from numpy import array, cross, sqrt
from numpy.linalg import solve


M = array([40, -40, -20])
I = array([ [2, -3, 0],
            [-3, 8, 0],
            [0, 0, 10]])
alpha = solve(I, M)
print(f"Alpha is {alpha}")

m = 12.
F = array([20, 0, 40])
acc_cm = F / m
r_P = array([-1, -1, 0])
acc_P = acc_cm + cross(alpha, r_P)
print("Acceleration of point P = -1i + -1j is")
print(acc_P)
print("Total acceleration is")
print(sqrt(acc_P.dot(acc_P)))