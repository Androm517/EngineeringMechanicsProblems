from numpy import array, cross, sqrt
from numpy.linalg import solve

Moment = [40, -40, -20]
Moment = array(Moment)
Inertia = [[2, -3, 0],
           [-3, 8, 0],
           [0, 0, 10]]
Inertia = array(Inertia)
alpha = solve(Inertia, Moment)
print(f"Alpha is: {alpha}")

mass = 12.
Force = array([20, 0, 40])
acc_cm = Force / mass
r_P = array([-1, -1, 0])
acc_P = acc_cm + cross(alpha, r_P)
print(f"Acceleration of point P = -1i + -1j is: {acc_P}")
print(f"Total acceleration is: {sqrt(acc_P.dot(acc_P))}")
